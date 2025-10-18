##                  easy.py                     ##
##      Expressive Abstract Syntax Yield        ##
##   Following CodePulse's tutorial on YouTube  ##
##              Made in Python3                 ##

##  Skipped Parts (just copied code)    ##
##  - Power Operators                   ##

#######################################
# IMPORTS
#######################################

from random import random
import sys
from strings_with_arrows import *

import string
import os
import math

#######################################
# CONSTANTS
#######################################

DIGITS = '0123456789'
LETTERS = string.ascii_letters
LETTERS_DIGITS = LETTERS + DIGITS

# Comment syntax - customize these to change comment style
COMMENT_START = '?>' # Single line comment start
COMMENT_BLOCK_START = 'note:' # Multi-line comment start 
COMMENT_BLOCK_END = ':note' # Multi-line comment end

#######################################
# ERRORS
#######################################

class Error:
    def __init__(self, pos_start, pos_end, error_name, details):
        self.pos_start = pos_start
        self.pos_end = pos_end
        self.error_name = error_name
        self.details = details
    
    def as_string(self):
        result  = f'{self.error_name}: {self.details}\n'
        result += f'File {self.pos_start.fn}, line {self.pos_start.ln + 1}'
        result += '\n\n' + string_with_arrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
        return result

class IllegalCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Illegal Character', details)

class ExpectedCharError(Error):
    def __init__(self, pos_start, pos_end, details):
        super().__init__(pos_start, pos_end, 'Expected Character', details)

class InvalidSyntaxError(Error):
    def __init__(self, pos_start, pos_end, details=''):
        super().__init__(pos_start, pos_end, 'Invalid Syntax', details)

class RTError(Error):
    def __init__(self, pos_start, pos_end, details, context):
        super().__init__(pos_start, pos_end, 'Runtime Error', details)
        self.context = context

    def as_string(self):
        result  = self.generate_traceback()
        result += f'{self.error_name}: {self.details}'
        result += '\n\n' + string_with_arrows(self.pos_start.ftxt, self.pos_start, self.pos_end)
        return result

    def generate_traceback(self):
        result = ''
        pos = self.pos_start
        ctx = self.context

        while ctx:
            result = f'  File {pos.fn}, line {str(pos.ln + 1)}, in {ctx.display_name}\n' + result
            pos = ctx.parent_entry_pos
            ctx = ctx.parent

        return 'Traceback (most recent call last):\n' + result

#######################################
# POSITION
#######################################

class Position:
    def __init__(self, idx, ln, col, fn, ftxt):
        self.idx = idx
        self.ln = ln
        self.col = col
        self.fn = fn
        self.ftxt = ftxt

    def advance(self, current_char=None):
        self.idx += 1
        self.col += 1

        if current_char == '\n':
            self.ln += 1
            self.col = 0

        return self

    def copy(self):
        return Position(self.idx, self.ln, self.col, self.fn, self.ftxt)

#######################################
# TOKENS
#######################################

TT_INT			= 'INT'
TT_FLOAT    	= 'FLOAT'
TT_TEXT         = 'TEXT'
TT_IDENTIFIER	= 'IDENTIFIER'
TT_KEYWORD		= 'KEYWORD'
TT_PLUS     	= 'PLUS'
TT_MINUS    	= 'MINUS'
TT_MUL      	= 'MUL'
TT_DIV      	= 'DIV'
TT_POW			= 'POW'
TT_EQ			= 'EQ'
TT_LPAREN   	= 'LPAREN'
TT_RPAREN   	= 'RPAREN'
TT_LSQUARE      = 'LSQUARE'
TT_RSQUARE      = 'RSQUARE'
TT_EE 			= 'EE'
TT_NE 			= 'NE'
TT_LT			= 'LT'
TT_GT 			= 'GT'
TT_LTE 			= 'LTE'
TT_GTE 			= 'GTE'
TT_COMMA        = 'COMMA'
TT_ARROW        = 'ARROW'
TT_NEWLINE      = 'NEWLINE'
TT_EOF			= 'EOF'

KEYWORDS = [
    # Variable setting Keywords
    'set',
    'to',

    # Arithmet Operators
    'plus',
    'minus',
    'times',
    'div',
    'pow',

    # List operation keywords
    'add',
    'remove',
    'merge',
    'get',

    # Some basic 'and' 'or' 'not' action
    'and',
    'or',
    'not',

    # If Keywords
    'if',
    'then',
    'nextif', # ts elif
    'otherwise', # ts else
    
    # Comparison Keywords
    'is',
    'isnt',
    'under',
    'above',
    'atmost',
    'atleast',

    # Loop Keywords (repeat i to/= 1 through 10 by 1 then)
    'repeat', # ts for
    'from', # ts =
    'through', # ts to
    'by', # ts step
    'while',
    'do', # ts then
    'give', # ts return
    'stop', # ts break
    'next', # ts continue

    # Functions
    'make', # ts def

    'end'
]

class Token:
    def __init__(self, type_, value=None, pos_start=None, pos_end=None):
        self.type = type_
        self.value = value

        if pos_start:
            self.pos_start = pos_start.copy()
            self.pos_end = pos_start.copy()
            self.pos_end.advance()

        if pos_end:
            self.pos_end = pos_end.copy()

    def matches(self, type_, value):
        return self.type == type_ and self.value == value
    
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'

#######################################
# LEXER
#######################################

class Lexer:
    def __init__(self, fn, text):
        self.fn = fn
        self.text = text
        self.pos = Position(-1, 0, -1, fn, text)
        self.current_char = None
        self.advance()
    
    def advance(self):
        self.pos.advance(self.current_char)
        self.current_char = self.text[self.pos.idx] if self.pos.idx < len(self.text) else None

    def peek_next(self):
        peek_idx = self.pos.idx + 1
        if peek_idx >= len(self.text):
            return None
        return self.text[peek_idx]

    def peek_ahead(self, n):
        peek_idx = self.pos.idx + n
        if peek_idx >= len(self.text):
            return None
        return self.text[peek_idx]

    def check_comment_start(self):
        if not self.current_char:
            return False
        # Match first character
        if self.current_char != COMMENT_START[0]:
            return False
        # Match second character if exists
        if len(COMMENT_START) > 1:
            next_char = self.peek_next()
            if next_char != COMMENT_START[1]:
                return False
        return True

    def check_block_comment_start(self):
        if not self.current_char:
            return False
        # Check if current character matches first character of block comment start
        if self.current_char != COMMENT_BLOCK_START[0]:
            return False
        # Check remaining characters
        for i in range(1, len(COMMENT_BLOCK_START)):
            if self.peek_ahead(i) != COMMENT_BLOCK_START[i]:
                return False
        return True

    def skip_comment(self):
        # Skip the comment start characters
        for _ in range(len(COMMENT_START)):
            self.advance()
        # Skip until end of line
        while self.current_char is not None and self.current_char != '\n':
            self.advance()

    def skip_block_comment(self):
        # Store starting position for error reporting
        pos_start = self.pos.copy()
        
        # Skip the comment start characters
        for _ in range(len(COMMENT_BLOCK_START)):
            self.advance()
            
        # Keep track of nested comments
        nesting_level = 1
        
        while self.current_char is not None and nesting_level > 0:
            # Check for nested block comment start
            if self.check_block_comment_start():
                for _ in range(len(COMMENT_BLOCK_START)):
                    self.advance()
                nesting_level += 1
                continue
                
            # Check for block comment end
            found_end = True
            for i, char in enumerate(COMMENT_BLOCK_END):
                peek_char = self.peek_ahead(i) if i == 0 else self.peek_ahead(i)
                if peek_char != char:
                    found_end = False
                    break
                    
            if found_end:
                for _ in range(len(COMMENT_BLOCK_END)):
                    self.advance()
                nesting_level -= 1
                continue
                
            self.advance()
            
        # If we reached EOF without finding the end comment marker
        if nesting_level > 0:
            return InvalidSyntaxError(
                pos_start, self.pos,
                f"Unclosed block comment. Expected '{COMMENT_BLOCK_END}'"
            )
            
        return None

    def make_tokens(self):
        tokens = []

        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char == '\n':
                tokens.append(Token(TT_NEWLINE, pos_start=self.pos))
                self.advance()
            elif self.check_comment_start():
                self.skip_comment()
            elif self.check_block_comment_start():
                error = self.skip_block_comment()
                if error: return [], error
            elif self.current_char == '.':
                tokens.append(Token(TT_NEWLINE, pos_start=self.pos))
                self.advance()
            elif self.current_char in DIGITS:
                tokens.append(self.make_number())
            elif self.current_char in LETTERS:
                tokens.append(self.make_identifier())
            elif self.current_char == '"':
                tokens.append(self.make_text())
            elif self.current_char == '+':
                tokens.append(Token(TT_PLUS, pos_start=self.pos))
                self.advance()
            elif self.current_char == '-':
                tokens.append(self.make_minus_or_arrow())
                self.advance()
            elif self.current_char == '*':
                tokens.append(Token(TT_MUL, pos_start=self.pos))
                self.advance()
            elif self.current_char == '/':
                tokens.append(Token(TT_DIV, pos_start=self.pos))
                self.advance()
            elif self.current_char == '^':
                tokens.append(Token(TT_POW, pos_start=self.pos))
                self.advance()
            elif self.current_char == '(':
                tokens.append(Token(TT_LPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char == ')':
                tokens.append(Token(TT_RPAREN, pos_start=self.pos))
                self.advance()
            elif self.current_char == '[':
                tokens.append(Token(TT_LSQUARE, pos_start=self.pos))
                self.advance()
            elif self.current_char == ']':
                tokens.append(Token(TT_RSQUARE, pos_start=self.pos))
                self.advance()
            elif self.current_char == '!':
                tok, error = self.make_not_equals()
                if error: return [], error
                tokens.append(tok)
            elif self.current_char == '=':
                tokens.append(self.make_equals())
            elif self.current_char == '<':
                tokens.append(self.make_less_than())
            elif self.current_char == '>':
                tokens.append(self.make_greater_than())
            elif self.current_char == ',':
                tokens.append(Token(TT_COMMA, pos_start=self.pos))
                self.advance()
            else:
                pos_start = self.pos.copy()
                char = self.current_char
                self.advance()
                return [], IllegalCharError(pos_start, self.pos, "'" + char + "'")

        tokens.append(Token(TT_EOF, pos_start=self.pos))
        return tokens, None

    def make_number(self):
        num_str = ''
        thent_repeat = 0
        pos_start = self.pos.copy()

        while self.current_char != None and (self.current_char in DIGITS or (self.current_char == '.' and self.peek_next() in DIGITS)):
            if self.current_char == '.':
                if thent_repeat == 1: break
                thent_repeat += 1
            num_str += self.current_char
            self.advance()

        if thent_repeat == 0:
            return Token(TT_INT, int(num_str), pos_start, self.pos)
        else:
            return Token(TT_FLOAT, float(num_str), pos_start, self.pos)

    def peek_next(self):
        if self.pos.idx + 1 < len(self.text):
            return self.text[self.pos.idx + 1]
        return None

    def make_text(self):
        text = ''
        pos_start = self.pos.copy()
        escape_character = False
        self.advance()

        escape_characters = {
            'n': '\n',
            't': '\t'
        }

        while self.current_char != None and (self.current_char != '"' or escape_character):
            if escape_character:
                text += escape_characters.get(self.current_char, self.current_char)
                escape_character = False
            else:
                if self.current_char == '\\':
                    escape_character = True
                else: 
                    text += self.current_char
            self.advance()
        
        self.advance()
        return Token(TT_TEXT, text, pos_start, self.pos)

    def make_identifier(self):
        id_str = ''
        pos_start = self.pos.copy()

        while self.current_char != None and self.current_char in LETTERS_DIGITS + '_':
            id_str += self.current_char
            self.advance()

        tok_type = TT_KEYWORD if id_str in KEYWORDS else TT_IDENTIFIER
        return Token(tok_type, id_str, pos_start, self.pos)

    def make_minus_or_arrow(self):
        tok_type = TT_MINUS
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '>':
            self.advance()
            tok_type = TT_ARROW

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_not_equals(self):
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            return Token(TT_NE, pos_start=pos_start, pos_end=self.pos), None

        self.advance()
        return None, ExpectedCharError(pos_start, self.pos, "'=' expected after '!'")
    
    def make_equals(self):
        tok_type = TT_EQ
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = TT_EE

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_less_than(self):
        tok_type = TT_LT
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = TT_LTE

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

    def make_greater_than(self):
        tok_type = TT_GT
        pos_start = self.pos.copy()
        self.advance()

        if self.current_char == '=':
            self.advance()
            tok_type = TT_GTE

        return Token(tok_type, pos_start=pos_start, pos_end=self.pos)

        while self.current_char != '\n':
            self.advance()

        self.advance()

#######################################
# NODES
#######################################

class NumberNode:
    def __init__(self, tok):
        self.tok = tok

        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self):
        return f'{self.tok}'

class TextNode:
    def __init__(self, tok):
        self.tok = tok

        self.pos_start = self.tok.pos_start
        self.pos_end = self.tok.pos_end

    def __repr__(self):
        return f'{self.tok}'

class ListNode:
    def __init__(self, element_nodes, pos_start, pos_end):
        self.element_nodes = element_nodes

        self.pos_start = pos_start
        self.pos_end = pos_end

class VarAccessNode:
    def __init__(self, var_name_tok):
        self.var_name_tok = var_name_tok

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.var_name_tok.pos_end

class VarAssignNode:
    def __init__(self, var_name_tok, value_node):
        self.var_name_tok = var_name_tok
        self.value_node = value_node

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.value_node.pos_end

class BinOpNode:
    def __init__(self, left_node, op_tok, right_node):
        self.left_node = left_node
        self.op_tok = op_tok
        self.right_node = right_node

        self.pos_start = self.left_node.pos_start
        self.pos_end = self.right_node.pos_end

    def __repr__(self):
        return f'({self.left_node}, {self.op_tok}, {self.right_node})'

class UnaryOpNode:
    def __init__(self, op_tok, node):
        self.op_tok = op_tok
        self.node = node

        self.pos_start = self.op_tok.pos_start
        self.pos_end = node.pos_end

    def __repr__(self):
        return f'({self.op_tok}, {self.node})'

class IfNode:
    def __init__(self, cases, otherwise_case):
        self.cases = cases
        self.otherwise_case = otherwise_case

        self.pos_start = self.cases[0][0].pos_start
        
        # Fix the pos_end calculation
        if self.otherwise_case:
            # otherwise_case is a tuple (expr, should_return_null)
            self.pos_end = self.otherwise_case[0].pos_end
        else:
            # Get the last case, which is a tuple (condition, expr, should_return_null) or (condition, expr)
            last_case = self.cases[len(self.cases) - 1]
            self.pos_end = last_case[1].pos_end  # The expr is at index 1

class RepeatNode:
    def __init__(self, var_name_tok, start_value_node, end_value_node, step_value_node, body_node, should_return_null):
        self.var_name_tok = var_name_tok
        self.start_value_node = start_value_node
        self.end_value_node = end_value_node
        self.step_value_node = step_value_node
        self.body_node = body_node
        self.should_return_null = should_return_null

        self.pos_start = self.var_name_tok.pos_start
        self.pos_end = self.body_node.pos_end

class WhileNode:
     def __init__(self, condition_node, body_node, should_return_null):
        self.condition_node = condition_node
        self.body_node = body_node
        self.should_return_null = should_return_null

        self.pos_start = self.condition_node.pos_start
        self.pos_end = self.body_node.pos_end

class FuncDefNode:
    def __init__(self, var_name_tok, arg_name_toks, body_node, should_auto_return):
        self.var_name_tok = var_name_tok
        self.arg_name_toks = arg_name_toks
        self.body_node = body_node
        self.should_auto_return = should_auto_return

        if self.var_name_tok:
            self.pos_start = self.var_name_tok.pos_start
        elif len(self.arg_name_toks) > 0:
            self.pos_start = self.arg_name_toks[0].pos_start
        else:
            self.pos_start = self.body_node.pos_start

        self.pos_end = self.body_node.pos_end

class CallNode:
    def __init__(self, node_to_call, arg_nodes):
        self.node_to_call = node_to_call
        self.arg_nodes = arg_nodes

        self.pos_start = self.node_to_call.pos_start

        if len(self.arg_nodes) > 0:
            self.pos_end = self.arg_nodes[len(self.arg_nodes) - 1].pos_end
        else:
            self.pos_end = self.node_to_call.pos_end

class GiveNode:
    def __init__(self, node_to_return, pos_start, pos_end):
        self.node_to_return = node_to_return

        self.pos_start = pos_start
        self.pos_end = pos_end

class NextNode:
    def __init__(self, pos_start, pos_end):
        self.pos_start = pos_start
        self.pos_end = pos_end

class StopNode:
    def __init__(self, pos_start, pos_end):
        self.pos_start = pos_start
        self.pos_end = pos_end

#######################################
# PARSE RESULT
#######################################

class ParseResult:
    def __init__(self):
        self.error = None
        self.node = None
        self.last_registered_advance_repeat = 0
        self.advance_repeat = 0
        self.to_reverse_repeat = 0

    def register_advancement(self):
        self.last_registered_advance_repeat = 1
        self.advance_repeat += 1

    def register(self, res):
        self.last_registered_advance_repeat = res.advance_repeat
        self.advance_repeat += res.advance_repeat
        if res.error: self.error = res.error
        return res.node

    def try_register(self, res):
        if res.error:
            self.to_reverse_repeat = res.advance_repeat
            return None
        return self.register(res)

    def success(self, node):
        self.node = node
        return self

    def failure(self, error):
        if not self.error or self.last_registered_advance_repeat == 0:
            self.error = error
        return self

#######################################
# PARSER
#######################################

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.tok_idx = -1
        self.advance()

    def advance(self, ):
        self.tok_idx += 1
        if self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]
        return self.current_tok

    def reverse(self, amount=1):
        self.tok_idx -= amount
        self.update_current_tok()
        return self.current_tok
    
    def update_current_tok(self):
        if self.tok_idx >= 0 and self.tok_idx < len(self.tokens):
            self.current_tok = self.tokens[self.tok_idx]

    def parse(self):
        res = self.statements()
        if not res.error and self.current_tok.type != TT_EOF:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected '+', '-', '*', '/' or '^'"
            ))
        return res

    ###################################

    def statements(self):
        res = ParseResult()
        statements = []
        pos_start = self.current_tok.pos_start.copy()

        while self.current_tok.type == TT_NEWLINE:
            res.register_advancement()
            self.advance()

        statement = res.register(self.statement())
        if res.error: return res   
        statements.append(statement)

        more_statements = True

        while True:
            newline_repeat = 0
            while self.current_tok.type == TT_NEWLINE:
                res.register_advancement()
                self.advance()
                newline_repeat += 1
            if newline_repeat == 0:
                more_statements = False

            if not more_statements: break
            statement = res.try_register(self.statement())
            if not statement:
                self.reverse(res.to_reverse_repeat)
                more_statements = False
                continue
            statements.append(statement)

        return res.success(ListNode(
            statements,
            pos_start,
            self.current_tok.pos_end.copy()
        ))

    def statement(self):
        res = ParseResult()
        pos_start = self.current_tok.pos_start.copy()

        if self.current_tok.matches(TT_KEYWORD, 'give'):
            res.register_advancement()
            self.advance()

            expr = res.try_register(self.expr())
            if not expr:
                self.reverse(res.to_reverse_repeat)
            return res.success(GiveNode(expr, pos_start, self.current_tok.pos_end.copy()))

        if self.current_tok.matches(TT_KEYWORD, 'next'):
            res.register_advancement()
            self.advance()
            return res.success(NextNode(pos_start, self.current_tok.pos_end.copy()))

        if self.current_tok.matches(TT_KEYWORD, 'stop'):
            res.register_advancement()
            self.advance()
            return res.success(StopNode(pos_start, self.current_tok.pos_end.copy()))

        expr = res.register(self.expr())
        if res.error: return res.failure(InvalidSyntaxError(
            self.current_tok.pos_start, self.current_tok.pos_end,
            "Expected 'give', 'next', 'stop' or expression"
        ))

        return res.success(expr)

    def if_expr(self):
        res = ParseResult()
        all_cases = res.register(self.if_expr_cases('if'))
        if res.error: return res
        cases, otherwise_case = all_cases
        return res.success(IfNode(cases, otherwise_case))

        # res = ParseResult()
        # cases = []
        # otherwise_case = None

        # if not self.current_tok.matches(TT_KEYWORD, 'if'):
        #     return res.failure(InvalidSyntaxError(
        #         self.current_tok.pos_start, self.current_tok.pos_end,
        #         f"Expected 'if'"
        #     ))

        # res.register_advancement()
        # self.advance()

        # condition = res.register(self.expr())
        # if res.error: return res

        # if not self.current_tok.matches(TT_KEYWORD, 'then'):
        #     return res.failure(InvalidSyntaxError(
        #         self.current_tok.pos_start, self.current_tok.pos_end,
        #         f"Expected 'then'"
        #     ))

        # res.register_advancement()
        # self.advance()

        # expr = res.register(self.expr())
        # if res.error: return res
        # cases.append((condition, expr))

        # while self.current_tok.matches(TT_KEYWORD, 'nextif'):
        #     res.register_advancement()
        #     self.advance()

        #     condition = res.register(self.expr())
        #     if res.error: return res

        #     if not self.current_tok.matches(TT_KEYWORD, 'then'):
        #         return res.failure(InvalidSyntaxError(
        #             self.current_tok.pos_start, self.current_tok.pos_end,
        #             f"Expected 'then'"
        #         ))

        #     res.register_advancement()
        #     self.advance()

        #     expr = res.register(self.expr())
        #     if res.error: return res
        #     cases.append((condition, expr))

        # if self.current_tok.matches(TT_KEYWORD, 'otherwise'):
        #     res.register_advancement()
        #     self.advance()

        #     otherwise_case = res.register(self.expr())
        #     if res.error: return res

        # return res.success(IfNode(cases, otherwise_case))

    def if_expr_b(self):
        return self.if_expr_cases('nextif')

    def if_expr_c(self):
        res = ParseResult()
        otherwise_case = None

        if self.current_tok.matches(TT_KEYWORD, 'otherwise'):
            res.register_advancement()
            self.advance()

            if self.current_tok.type == TT_NEWLINE:
                res.register_advancement()
                self.advance()

                statements = res.register(self.statements())
                if res.error: return res
                otherwise_case = (statements, True)

                if self.current_tok.matches(TT_KEYWORD, 'end'):
                    res.register_advancement()
                    self.advance()
                else:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        f"Expected 'end'"
                    ))
            else:
                expr = res.register(self.expr())
                if res.error: return res
                otherwise_case = (expr, False)

        return res.success(([], otherwise_case))

    def if_expr_b_or_c(self):
        res = ParseResult()
        cases, otherwise_case = [], None

        if self.current_tok.matches(TT_KEYWORD, 'nextif'):
            all_cases = res.register(self.if_expr_b())
            if res.error: return res
            cases, otherwise_case = all_cases
        else:
            # FIX: Unpack the tuple returned by if_expr_c
            all_cases = res.register(self.if_expr_c())
            if res.error: return res
            cases, otherwise_case = all_cases  # Unpack properly

        return res.success((cases, otherwise_case))

    def if_expr_cases(self, case_keyword):
        res = ParseResult()
        cases = []
        otherwise_case = None

        if not self.current_tok.matches(TT_KEYWORD, case_keyword):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected '{case_keyword}'"
            ))
        
        res.register_advancement()
        self.advance()

        condition = res.register(self.expr())
        if res.error: return res

        if not self.current_tok.matches(TT_KEYWORD, 'then'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'then'"
            ))
        
        res.register_advancement()
        self.advance()

        if self.current_tok.type == TT_NEWLINE:
            res.register_advancement()
            self.advance()

            statements = res.register(self.statements())
            if res.error: return res
            cases.append((condition, statements, True))

            if self.current_tok.matches(TT_KEYWORD, 'end'):
                res.register_advancement()
                self.advance()
            else:
                all_cases = res.register(self.if_expr_b_or_c())
                if res.error: return res
                new_cases, otherwise_case = all_cases
                cases.extend(new_cases)
        else:
            expr = res.register(self.statement())
            if res.error: return res
            cases.append((condition, expr, False))

            all_cases = res.register(self.if_expr_b_or_c())
            if res.error: return res
            new_cases, otherwise_case = all_cases
            cases.extend(new_cases)

        return res.success((cases, otherwise_case))

    def repeat_expr(self):
        res = ParseResult()

        if not self.current_tok.matches(TT_KEYWORD, 'repeat'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'repeat'"
            ))

        res.register_advancement()
        self.advance()

        if self.current_tok.type != TT_IDENTIFIER:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected identifier"
            ))

        var_name = self.current_tok
        res.register_advancement()
        self.advance()

        if not (self.current_tok.type == TT_EQ or self.current_tok.matches(TT_KEYWORD, 'from')):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'from' or '='"
            ))
        
        res.register_advancement()
        self.advance()

        start_value = res.register(self.expr())
        if res.error: return res

        if not self.current_tok.matches(TT_KEYWORD, 'through'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'through'"
            ))
        
        res.register_advancement()
        self.advance()

        end_value = res.register(self.expr())
        if res.error: return res

        if self.current_tok.matches(TT_KEYWORD, 'by'):
            res.register_advancement()
            self.advance()

            step_value = res.register(self.expr())
            if res.error: return res
        else:
            step_value = None

        if not self.current_tok.matches(TT_KEYWORD, 'do'):  # Changed from 'then' to 'do'
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'do'"  # Updated error message
            ))

        res.register_advancement()
        self.advance()

        if self.current_tok.type == TT_NEWLINE:
            res.register_advancement()
            self.advance()

            body = res.register(self.statements())
            if res.error: return res

            if not self.current_tok.matches(TT_KEYWORD, 'end'):
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected 'end'"
                ))
            
            res.register_advancement()
            self.advance()

            return res.success(RepeatNode(var_name, start_value, end_value, step_value, body, True))
        
        body = res.register(self.statement())
        if res.error: return res

        return res.success(RepeatNode(var_name, start_value, end_value, step_value, body, False))

    def while_expr(self):
        res = ParseResult()

        if not self.current_tok.matches(TT_KEYWORD, 'while'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'while'"
            ))

        res.register_advancement()
        self.advance()

        condition = res.register(self.expr())
        if res.error: return res

        if not self.current_tok.matches(TT_KEYWORD, 'then'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'then'"
            ))

        res.register_advancement()
        self.advance()

        if self.current_tok.type == TT_NEWLINE:
            res.register_advancement()
            self.advance()

            body = res.register(self.statements())
            if res.error: return res

            if not self.current_tok.matches(TT_KEYWORD, 'end'):
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected 'end'"
                ))
            
            res.register_advancement()
            self.advance()

            return res.success(WhileNode(condition, body, True))

        body = res.register(self.statement())
        if res.error: return res

        return res.success(WhileNode(condition, body, False))

    def call(self):
        res = ParseResult()
        atom = res.register(self.atom())
        if res.error: return res

        if self.current_tok.type == TT_LPAREN:
            res.register_advancement()
            self.advance()
            arg_nodes = []

            if self.current_tok.type == TT_RPAREN:
                res.register_advancement()
                self.advance()
            else:
                arg_nodes.append(res.register(self.expr()))
                if res.error:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        "Expected ')', 'if', 'set', 'repeat', 'while', 'make', int, float, identifier, '+', '-', '(', '[', or 'not'"
                    ))

                while self.current_tok.type == TT_COMMA:
                    res.register_advancement()
                    self.advance()

                    arg_nodes.append(res.register(self.expr()))
                    if res.error: return res

                if self.current_tok.type != TT_RPAREN:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        f"Expected ',' or ')'"
                    ))

                res.register_advancement()
                self.advance()

            return res.success(CallNode(atom, arg_nodes))
        
        return res.success(atom)

    def atom(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in (TT_INT, TT_FLOAT):
            res.register_advancement()
            self.advance()
            return res.success(NumberNode(tok))

        if tok.type in TT_TEXT:
            res.register_advancement()
            self.advance()
            return res.success(TextNode(tok))

        elif tok.type == TT_IDENTIFIER:
            res.register_advancement()
            self.advance()
            return res.success(VarAccessNode(tok))

        elif tok.type == TT_LPAREN:
            res.register_advancement()
            self.advance()
            expr = res.register(self.expr())
            if res.error: return res
            if self.current_tok.type == TT_RPAREN:
                res.register_advancement()
                self.advance()
                return res.success(expr)
            else:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected ')'"
                ))

        elif tok.type == TT_LSQUARE:
            list_expr = res.register(self.list_expr())
            if res.error: return res
            return res.success(list_expr)
        
        elif tok.matches(TT_KEYWORD, 'if'):
            if_expr = res.register(self.if_expr())
            if res.error: return res
            return res.success(if_expr)

        elif tok.matches(TT_KEYWORD, 'repeat'):
            repeat_expr = res.register(self.repeat_expr())
            if res.error: return res
            return res.success(repeat_expr)

        elif tok.matches(TT_KEYWORD, 'while'):
            while_expr = res.register(self.while_expr())
            if res.error: return res
            return res.success(while_expr)

        elif tok.matches(TT_KEYWORD, 'make'):
            func_def = res.register(self.func_def())
            if res.error: return res
            return res.success(func_def)

        return res.failure(InvalidSyntaxError(
            tok.pos_start, tok.pos_end,
            "Expected 'set', 'if', 'repeat', 'while', 'make', int, float, identifier, '+', '-', '(', '[', 'if', 'repeat', 'while', or 'make'"
        ))

    def list_expr(self):
        res = ParseResult()
        element_nodes = []
        pos_start = self.current_tok.pos_start.copy()

        if self.current_tok.type != TT_LSQUARE:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected '['"
            ))

        res.register_advancement()
        self.advance()

        if self.current_tok.type == TT_RSQUARE:
            res.register_advancement()
            self.advance()
        else:
            element_nodes.append(res.register(self.expr()))
            if res.error:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected ']', 'if', 'set', 'repeat', 'while', 'make', int, float, identifier, '+', '-', '(', '[', or 'not'"
                ))

            while self.current_tok.type == TT_COMMA:
                res.register_advancement()
                self.advance()

                element_nodes.append(res.register(self.expr()))
                if res.error: return res

            if self.current_tok.type != TT_RSQUARE:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    f"Expected ',' or ']'"
                ))

            res.register_advancement()
            self.advance()

        return res.success(ListNode(
            element_nodes, pos_start,
            self.current_tok.pos_end.copy()
        ))


    def power(self):
        return self.bin_op(self.call, (TT_POW, (TT_KEYWORD, 'pow')), self.factor)

    def factor(self):
        res = ParseResult()
        tok = self.current_tok

        if tok.type in (TT_PLUS, TT_MINUS):
            res.register_advancement()
            self.advance()
            factor = res.register(self.factor())
            if res.error: return res
            return res.success(UnaryOpNode(tok, factor))

        return self.power()

    def term(self):
        return self.bin_op(self.factor, (
            TT_MUL, TT_DIV,
            (TT_KEYWORD, 'times'),
            (TT_KEYWORD, 'div'),
            (TT_KEYWORD, 'merge'),
            (TT_KEYWORD, 'get')
        ))

    def arith_expr(self):
        return self.bin_op(self.term, (
            TT_PLUS, TT_MINUS,
            (TT_KEYWORD, 'plus'),
            (TT_KEYWORD, 'minus'),
            (TT_KEYWORD, 'add'),
            (TT_KEYWORD, 'remove')
        ))

    def comp_expr(self):
        res = ParseResult()

        if self.current_tok.matches(TT_KEYWORD, 'not'):
            op_tok = self.current_tok
            res.register_advancement()
            self.advance()

            node = res.register(self.comp_expr())
            if res.error: return res
            return res.success(UnaryOpNode(op_tok, node))

        node = res.register(self.bin_op(self.arith_expr, (
            TT_EE, TT_NE, TT_LT, TT_GT, TT_LTE, TT_GTE,
            (TT_KEYWORD, 'is'),
            (TT_KEYWORD, 'isnt'),
            (TT_KEYWORD, 'under'),
            (TT_KEYWORD, 'above'),
            (TT_KEYWORD, 'atmost'),
            (TT_KEYWORD, 'atleast')
        )))

        if res.error:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected int, float, identifier, '+', '-', '(', '[', or 'not'"
            ))

        return res.success(node)

    def expr(self):
        res = ParseResult()

        if self.current_tok.matches(TT_KEYWORD, 'set'):
            res.register_advancement()
            self.advance()

            if self.current_tok.type != TT_IDENTIFIER:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected identifier"
                ))

            var_name = self.current_tok
            res.register_advancement()
            self.advance()

            # Accept both '=' and 'to' keyword
            if self.current_tok.type == TT_EQ or self.current_tok.matches(TT_KEYWORD, 'to'):
                res.register_advancement()
                self.advance()
            else:
                return res.failure(InvalidSyntaxError(
                    self.current_tok.pos_start, self.current_tok.pos_end,
                    "Expected '=' or 'to'"
                ))

            expr = res.register(self.expr())
            if res.error: return res
            return res.success(VarAssignNode(var_name, expr))

        node = res.register(self.bin_op(self.comp_expr, ((TT_KEYWORD, "and"), (TT_KEYWORD, "or"))))

        if res.error:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                "Expected 'set', 'if', 'repeat', 'while', 'make', int, float, identifier, '+', '-', '(', '[', or 'not'"
            ))

        return res.success(node)

    def func_def(self):
        res = ParseResult()

        if not self.current_tok.matches(TT_KEYWORD, 'make'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'make'"
            ))

        res.register_advancement()
        self.advance()

        if self.current_tok.type == TT_IDENTIFIER:
            var_name_tok = self.current_tok
            res.register_advancement()
            self.advance()
            if self.current_tok.type != TT_LPAREN:
                return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected '('"
            ))
        else:
            var_name_tok = None
            if self.current_tok.type != TT_LPAREN:
                return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected identifier or '('"
            ))

        res.register_advancement()
        self.advance()
        arg_name_toks = []

        if self.current_tok.type == TT_IDENTIFIER:
            arg_name_toks.append(self.current_tok)
            res.register_advancement()
            self.advance()

            while self.current_tok.type == TT_COMMA:
                res.register_advancement()
                self.advance()

                if self.current_tok.type != TT_IDENTIFIER:
                    return res.failure(InvalidSyntaxError(
                        self.current_tok.pos_start, self.current_tok.pos_end,
                        f"Expected identifier"
                    ))

                arg_name_toks.append(self.current_tok)
                res.register_advancement()
                self.advance()

            if self.current_tok.type != TT_RPAREN:
                return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected ',' or ')'"
            ))
        else:
            if self.current_tok.type != TT_RPAREN:
                return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected identifier or ')'"
            ))

        res.register_advancement()
        self.advance()

        if self.current_tok.type == TT_ARROW:
            res.register_advancement()
            self.advance()
            node_to_return = res.register(self.expr())
            if res.error: return res

            return res.success(FuncDefNode(
                var_name_tok,
                arg_name_toks,
                node_to_return,
                True
            ))
        
        if self.current_tok.type != TT_NEWLINE:
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected '->' or NEWLINE"
            ))
        
        res.register_advancement()
        self.advance()

        body = res.register(self.statements())
        if res.error: return res

        if not self.current_tok.matches(TT_KEYWORD, 'end'):
            return res.failure(InvalidSyntaxError(
                self.current_tok.pos_start, self.current_tok.pos_end,
                f"Expected 'end'"
            ))
        
        res.register_advancement()
        self.advance()

        return res.success(FuncDefNode(
            var_name_tok,
            arg_name_toks,
            body,
            False
        ))


    ###################################

    def bin_op(self, func_a, ops, func_b=None):
        if func_b == None:
            func_b = func_a
        
        res = ParseResult()
        left = res.register(func_a())
        if res.error: return res

        while self.current_tok.type in ops or (self.current_tok.type, self.current_tok.value) in ops:
            op_tok = self.current_tok
            res.register_advancement()
            self.advance()
            right = res.register(func_b())
            if res.error: return res
            left = BinOpNode(left, op_tok, right)

        return res.success(left)

#######################################
# RUNTIME RESULT
#######################################

class RTResult:
    def __init__(self):
        self.reset()

    def reset(self):
        self.value = None
        self.error = None
        self.func_return_value = None
        self.loop_should_continue = False
        self.loop_should_break = False

    def register(self, res):
        if res.error: self.error = res.error
        if res.func_return_value: self.func_return_value = res.func_return_value
        if res.loop_should_continue: self.loop_should_continue = True
        if res.loop_should_break: self.loop_should_break = True
        return res.value

    def success(self, value):
        self.reset()
        self.value = value
        return self

    def success_return(self, value):
        self.reset()
        self.func_return_value = value
        return self
    
    def success_continue(self):
        self.reset()
        self.loop_should_continue = True
        return self
    
    def success_break(self):
        self.reset()
        self.loop_should_break = True
        return self

    def failure(self, error):
        self.reset()
        self.error = error
        return self

    def should_return(self):
        return (
            self.error or
            self.func_return_value or
            self.loop_should_continue or
            self.loop_should_break
        )

#######################################
# VALUES
#######################################

class Value:
    def __init__(self):
        self.set_pos()
        self.set_context()

    def set_pos(self, pos_start=None, pos_end=None):
        self.pos_start = pos_start
        self.pos_end = pos_end
        return self

    def set_context(self, context=None):
        self.context = context
        return self

    def added_to(self, other):
        return None, self.illegal_operation(other)

    def subbed_by(self, other):
        return None, self.illegal_operation(other)

    def timesed_by(self, other):
        return None, self.illegal_operation(other)

    def dived_by(self, other):
        return None, self.illegal_operation(other)

    def powed_by(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_eq(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_ne(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_lt(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_gt(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_lte(self, other):
        return None, self.illegal_operation(other)

    def get_comparison_gte(self, other):
        return None, self.illegal_operation(other)

    def anded_by(self, other):
        return None, self.illegal_operation(other)

    def ored_by(self, other):
        return None, self.illegal_operation(other)

    def notted(self, other):
        return None, self.illegal_operation(other)

    def execute(self, args):
        return RTResult().failure(self.illegal_operation())

    def copy(self):
        raise Exception('No copy method defined')

    def is_true(self):
        return False

    def illegal_operation(self, other=None):
        if not other: other = self
        return RTError(
            self.pos_start, other.pos_end,
            'Illegal operation',
            self.context
        )

class Number(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def added_to(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def subbed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def timesed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value * other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def dived_by(self, other):
        if isinstance(other, Number):
            if other.value == 0:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Division by zero is not allowed',
                    self.context
                )

            return Number(self.value / other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def powed_by(self, other):
        if isinstance(other, Number):
            return Number(self.value ** other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_eq(self, other):
        if isinstance(other, Number):
            return Number(int(self.value == other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_ne(self, other):
        if isinstance(other, Number):
            return Number(int(self.value != other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_lt(self, other):
        if isinstance(other, Number):
            return Number(int(self.value < other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gt(self, other):
        if isinstance(other, Number):
            return Number(int(self.value > other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_lte(self, other):
        if isinstance(other, Number):
            return Number(int(self.value <= other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def get_comparison_gte(self, other):
        if isinstance(other, Number):
            return Number(int(self.value >= other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def anded_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value and other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def ored_by(self, other):
        if isinstance(other, Number):
            return Number(int(self.value or other.value)).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def notted(self):
        return Number(1 if self.value == 0 else 0).set_context(self.context), None

    def copy(self):
        copy = Number(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def is_true(self):
        return self.value != 0
    
    def __repr__(self):
        return str(self.value)

Number.null = Number(0)

Number.false = Number(0)
Number.false.is_boolean = True

Number.true = Number(1)
Number.true.is_boolean = True

Number.math_PI = Number(math.pi)

class Text(Value):
    def __init__(self, value):
        super().__init__()
        self.value = value

    def added_to(self, other):
        if isinstance(other, Text):
            return Text(self.value + other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def timesed_by(self, other):
        if isinstance(other, Number):
            return Text(self.value * other.value).set_context(self.context), None
        else:
            return None, Value.illegal_operation(self, other)

    def is_true(self):
        return len(self.value) > 0

    def copy(self):
        copy = Text(self.value)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __str__(self):
        return self.value

    def __repr__(self): return f'"{self.value}"'

class List(Value):
    def __init__(self, elements):
        super().__init__()
        self.elements = elements

    def added_to(self, other):
        new_list = self.copy()
        new_list.elements.append(other)
        return new_list, None

    def subbed_by(self, other):
        if isinstance(other, Number):
            new_list = self.copy()
            try:
                new_list.elements.pop(other.value)
                return new_list, None
            except:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Element at index couldn\'t be removed from list: Index out of bounds',
                    self.context
                )
        else:
            return None, Value.illegal_operation(self, other)

    def timesed_by(self, other):
        if isinstance(other, List):
            new_list = self.copy()
            new_list.elements.extend(other.elements)
            return new_list, None
        else:
            return None, Value.illegal_operation(self, other)

    def dived_by(self, other):
        if isinstance(other, Number):
            try:
                return self.elements[other.value], None
            except:
                return None, RTError(
                    other.pos_start, other.pos_end,
                    'Element at index couldn\'t be retrieved from list: Index out of bounds',
                    self.context
                )
        else:
            return None, Value.illegal_operation(self, other)

    def copy(self):
        copy = List(self.elements)
        copy.set_pos(self.pos_start, self.pos_end)
        copy.set_context(self.context)
        return copy

    def __str__(self):
        return f", ".join([str(x) for x in self.elements])

    def __repr__(self):
        return f'[{", ".join([str(x) for x in self.elements])}]'

class BaseFunction(Value):
    def __init__(self, name):
        super().__init__()
        self.name = name or "<micro>"

    def generate_new_context(self):
        new_context = Context(self.name, self.context, self.pos_start)
        new_context.symbol_table = SymbolTable(new_context.parent.symbol_table)
        return new_context

    def if_args(self, arg_names, args):
        res = RTResult()

        if len(args) > len(arg_names):
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"{len(args) - len(arg_names)} too many arguments passed into '{self.name}'",
                self.context
            ))
        
        if len(args) < len(arg_names):
            return res.failure(RTError(
                self.pos_start, self.pos_end,
                f"{len(arg_names) - len(args)} too few arguments passed into '{self.name}'",
                self.context
            ))
        
        return res.success(None)

    def populate_args(self, arg_names, args, exec_ctx):
        for i in range(len(args)):
            arg_name = arg_names[i]
            arg_value = args[i]
            arg_value.set_context(exec_ctx)
            exec_ctx.symbol_table.set(arg_name, arg_value)

    def if_and_populate_args(self, arg_names, args, exec_ctx):
        res = RTResult()
        res.register(self.if_args(arg_names, args))
        if res.should_return(): return res
        self.populate_args(arg_names, args, exec_ctx)
        return res.success(None)

class Function(BaseFunction):
    def __init__(self, name, body_node, arg_names, should_auto_return):
        super().__init__(name)
        self.body_node = body_node
        self.arg_names = arg_names
        self.should_auto_return = should_auto_return
    
    def execute(self, args): 
        res = RTResult()
        interpreter = Interpreter()
        exec_ctx = self.generate_new_context()

        res.register(self.if_and_populate_args(self.arg_names, args, exec_ctx))
        if res.should_return(): return res

        value = res.register(interpreter.visit(self.body_node, exec_ctx))
        if res.should_return() and res.func_return_value == None: return res

        ret_value = (value if self.should_auto_return else None) or res.func_return_value or Number.null
        return res.success(ret_value)

    def copy(self):
        copy = Function(self.name, self.body_node, self.arg_names, self.should_auto_return)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f"<function {self.name}>"

class BuiltInFunction(BaseFunction):
    def __init__(self, name):
        super().__init__(name)
    
    def execute(self, args):
        res = RTResult()
        exec_ctx = self.generate_new_context()

        method_name = f'execute_{self.name}'
        method = getattr(self, method_name, self.no_visit_method)

        res.register(self.if_and_populate_args(method.arg_names, args, exec_ctx))
        if res.should_return(): return res

        return_value = res.register(method(exec_ctx))
        if res.should_return(): return res

        return res.success(return_value)

    def no_visit_method(self, node, context):
        raise Exception(f'No execute {self.name} method defined')

    def copy(self):
        copy = BuiltInFunction(self.name)
        copy.set_context(self.context)
        copy.set_pos(self.pos_start, self.pos_end)
        return copy

    def __repr__(self):
        return f'<built-in function {self.name}>'

    ###################################

    def execute_say(self, exec_ctx):
        print(str(exec_ctx.symbol_table.get('value')))
        return RTResult().success(Number.null)
    execute_say.arg_names = ['value']

    def execute_saySave(self, exec_ctx):
        return RTResult().success(Text(str(exec_ctx.symbol_table.get('value'))))
    execute_saySave.arg_names = ['value']

    def execute_ask(self, exec_ctx):
        text = input()
        return RTResult().success(Text(text))
    execute_ask.arg_names = []

    def execute_askNumber(self, exec_ctx):
        while True:
            number = input()
            try:
                number = int(number)
                break
            except ValueError:
                print(f"'{number} must be an integer (no decimals). Try again!")
        return RTResult().success(Number(number))
    execute_askNumber.arg_names = []

    def execute_clean(self, exec_ctx):
        os.system('cls' if os.name == 'nt' else 'clear')
        return RTResult().success(Number.null)
    execute_clean.arg_names = []

    def execute_isNumber(self, exec_ctx):
        isNumber = isinstance(exec_ctx.symbol_table.get("value"), Number)
        return RTResult().success(Number.true if isNumber else Number.false)
    execute_isNumber.arg_names = ['value']

    def execute_isText(self, exec_ctx):
        isText = isinstance(exec_ctx.symbol_table.get("value"), Text)
        return RTResult().success(Number.true if isText else Number.false)
    execute_isText.arg_names = ['value']

    def execute_isList(self, exec_ctx):
        isList = isinstance(exec_ctx.symbol_table.get("value"), List)
        return RTResult().success(Number.true if isList else Number.false)
    execute_isList.arg_names = ['value']

    def execute_isFunction(self, exec_ctx):
        isFunction = isinstance(exec_ctx.symbol_table.get("value"), BaseFunction)
        return RTResult().success(Number.true if isFunction else Number.false)
    execute_isFunction.arg_names = ['value']

    def execute_append(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        value = exec_ctx.symbol_table.get("value")

        if not isinstance(list_, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))

        list_.elements.append(value)
        return RTResult().success(Number.null)
    execute_append.arg_names = ['list', 'value']

    def execute_pop(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")
        index = exec_ctx.symbol_table.get("index")

        if not isinstance(list_, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))

        if not isinstance(index, Number):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be number",
                exec_ctx
            ))

        try:
            element = list_.elements.pop(index.value)
        except:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                'Element at this index could not be removed from list because index is out of bounds',
                exec_ctx
            ))
        return RTResult().success(element)
    execute_pop.arg_names = ["list", "index"]

    def execute_extend(self, exec_ctx):
        listA = exec_ctx.symbol_table.get("listA")
        listB = exec_ctx.symbol_table.get("listB")

        if not isinstance(listA, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "First argument must be list",
                exec_ctx
            ))

        if not isinstance(listB, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Second argument must be list",
                exec_ctx
            ))

        listA.elements.extend(listB.elements)
        return RTResult().success(Number.null)
    execute_extend.arg_names = ["listA", "listB"]

    def execute_lengthOf(self, exec_ctx):
        list_ = exec_ctx.symbol_table.get("list")

        if not isinstance(list_, List):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Argument must be list",
                exec_ctx
            ))

        return RTResult().success(Number(len(list_.elements)))
    execute_lengthOf.arg_names = ["list"]

    def execute_run(self, exec_ctx):
        filename = exec_ctx.symbol_table.get("filename")

        if not isinstance(filename, Text):
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                "Argument must be text",
                exec_ctx
            ))

        fn = filename.value
        if not fn.endswith('.esy'):
            fn += '.esy'

        try:
            with open(fn, "r") as f:
                script = f.read()
        except FileNotFoundError:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Script '{fn}' not found",
                exec_ctx
            ))
        except Exception as e:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to load script '{fn}'\n" + str(e),
                exec_ctx
            ))

        _, error = run(fn, script)
        if error:
            return RTResult().failure(RTError(
                self.pos_start, self.pos_end,
                f"Failed to finish executing script '{fn}'\n" + error.as_string(),
                exec_ctx
            ))

        return RTResult().success(Number.null)
    execute_run.arg_names = ["filename"]

    # def execute_random(self, exec_ctx):
    #     min_ = exec_ctx.symbol_table.get("min")
    #     max_ = exec_ctx.symbol_table.get("max")

    #     if not isinstance(min_, Number) or not isinstance(max_, Number):
    #         return RTResult().failure(RTError(
    #             self.pos_start, self.pos_end,
    #             "Arguments must be numbers",
    #             exec_ctx
    #         ))

    #     if min_.value > max_.value:
    #         return RTResult().failure(RTError(
    #             self.pos_start, self.pos_end,
    #             "Min cannot be greater than max",
    #             exec_ctx
    #         ))

    #     rand_value = random.randint(min_.value, max_.value)
    #     return RTResult().success(Number(rand_value))
    # execute_random.arg_names = ["min", "max"]

    # ---------- Type & Casting Built-ins ----------
    def execute_typeOf(self, exec_ctx):
        """typeOf(value) -> Text('Number'|'Text'|'List'|'Function'|'null')"""
        value = exec_ctx.symbol_table.get("value")
        if isinstance(value, Number):
            return RTResult().success(Text("Number"))
        if isinstance(value, Text):
            return RTResult().success(Text("Text"))
        if isinstance(value, List):
            return RTResult().success(Text("List"))
        if isinstance(value, BaseFunction):
            return RTResult().success(Text("Function"))
        if value is None:
            return RTResult().success(Text("null"))
        # fallback
        return RTResult().success(Text(str(type(value))))
    execute_typeOf.arg_names = ['value']

    def execute_toNumber(self, exec_ctx):
        """toNumber(value) -> Number or runtime error if conversion fails"""
        value = exec_ctx.symbol_table.get("value")

        # already a Number
        if isinstance(value, Number):
            return RTResult().success(value.copy())

        # Text -> try parse
        if isinstance(value, Text):
            s = value.value.strip()
            try:
                if '.' in s:
                    n = float(s)
                else:
                    n = int(s)
                return RTResult().success(Number(n))
            except Exception:
                return RTResult().failure(RTError(
                    self.pos_start, self.pos_end,
                    f"Cannot cast '{s}' to Number",
                    exec_ctx
                ))

        # List of single numeric element? attempt to extract
        if isinstance(value, List) and len(value.elements) == 1 and isinstance(value.elements[0], Number):
            return RTResult().success(value.elements[0].copy())

        # Otherwise illegal
        return RTResult().failure(RTError(
            self.pos_start, self.pos_end,
            "toNumber() requires a Number or numeric Text",
            exec_ctx
        ))
    execute_toNumber.arg_names = ['value']

    def execute_toText(self, exec_ctx):
        """toText(value) -> Text
        - Boolean singletons (Number.true / Number.false): "true"/"false"
        - Number: numeric string (integers shown without .0)
        - Text: unchanged
        - List: string representation via List.__str__
        - Function: repr()
        - None: "null"
        - Fallback: str(value)
        """
        value = exec_ctx.symbol_table.get("value")

        # Text -> return copy
        if isinstance(value, Text):
            return RTResult().success(value.copy())

        # Number -> check boolean singletons first
        if isinstance(value, Number):
            # If this Number instance was explicitly marked as a boolean singleton,
            # return "true"/"false".
            if getattr(value, "is_boolean", False):
                return RTResult().success(Text("true" if float(value.value) == 1.0 else "false"))

            # Otherwise print numbers normally: integers without ".0"
            try:
                # handle integers without .0
                if isinstance(value.value, int) or (isinstance(value.value, float) and value.value.is_integer()):
                    return RTResult().success(Text(str(int(value.value))))
            except Exception:
                pass

            return RTResult().success(Text(str(value.value)))

        # List -> use existing string representation
        if isinstance(value, List):
            return RTResult().success(Text(str(value)))

        # Function / Built-in -> repr
        if isinstance(value, BaseFunction):
            return RTResult().success(Text(repr(value)))

        # None -> "null"
        if value is None:
            return RTResult().success(Text("null"))

        # Fallback -> str()
        return RTResult().success(Text(str(value)))
    execute_toText.arg_names = ['value']


    def execute_toList(self, exec_ctx):
        """toList(value) -> List: if value is list -> copy, else -> [value]"""
        value = exec_ctx.symbol_table.get("value")

        if isinstance(value, List):
            return RTResult().success(value.copy())
        # wrap other values into a single-element list (copy where possible)
        if hasattr(value, 'copy'):
            elem = value.copy()
        else:
            elem = value
        return RTResult().success(List([elem]))
    execute_toList.arg_names = ['value']

    def execute_toState(self, exec_ctx):
        """
        toState(value) -> Number.true (1) or Number.false (0)
        Rules:
          - Number: 0 -> false, anything else -> true
          - Text: trimmed lowercase "true","t","yes","y","1" -> true;
                  "false","f","no","n","0" or "" -> false;
                  otherwise try numeric parse (non-zero -> true), else false
          - List: non-empty -> true, empty -> false
          - Function (BaseFunction): true
          - None: false
          - Fallback: false
        """
        value = exec_ctx.symbol_table.get("value")

        # Numbers
        if isinstance(value, Number):
            return RTResult().success(Number.true if value.value != 0 else Number.false)

        # Text
        if isinstance(value, Text):
            s = value.value.strip().lower()
            if s in ("true", "t", "yes", "y", "1"):
                return RTResult().success(Number.true)
            if s in ("false", "f", "no", "n", "0", ""):
                return RTResult().success(Number.false)
            # try numeric parse
            try:
                if '.' in s:
                    n = float(s)
                else:
                    n = int(s)
                return RTResult().success(Number.true if n != 0 else Number.false)
            except Exception:
                # not parseable — treat as false (non-strict)
                return RTResult().success(Number.false)

        # List
        if isinstance(value, List):
            return RTResult().success(Number.true if len(value.elements) > 0 else Number.false)

        # Functions / builtins
        if isinstance(value, BaseFunction):
            return RTResult().success(Number.true)

        # None or unknown -> false
        if value is None:
            return RTResult().success(Number.false)

        # Fallback: try truthiness via Python bool (conservative)
        try:
            py_truth = bool(value)
            return RTResult().success(Number.true if py_truth else Number.false)
        except Exception:
            return RTResult().success(Number.false)
    execute_toState.arg_names = ['value']

#######################################
# INITIALIZE BUILT-IN FUNCTIONS

# BuiltInFunction.random      = BuiltInFunction("random")
BuiltInFunction.say         = BuiltInFunction("say")
BuiltInFunction.saySave     = BuiltInFunction("saySave")
BuiltInFunction.ask         = BuiltInFunction("ask")
BuiltInFunction.askNumber   = BuiltInFunction("askNumber")
BuiltInFunction.clean       = BuiltInFunction("clean")
BuiltInFunction.isNumber    = BuiltInFunction("isNumber")
BuiltInFunction.isText      = BuiltInFunction("isText")
BuiltInFunction.isList      = BuiltInFunction("isList")
BuiltInFunction.isFunction  = BuiltInFunction("isFunction")
BuiltInFunction.append      = BuiltInFunction("append")
BuiltInFunction.pop         = BuiltInFunction("pop")
BuiltInFunction.extend      = BuiltInFunction("extend")
BuiltInFunction.lengthOf    = BuiltInFunction("lengthOf")
BuiltInFunction.run         = BuiltInFunction("run")
BuiltInFunction.typeOf      = BuiltInFunction("typeOf")
BuiltInFunction.toNumber    = BuiltInFunction("toNumber")
BuiltInFunction.toText      = BuiltInFunction("toText")
BuiltInFunction.toList      = BuiltInFunction("toList")
BuiltInFunction.toState     = BuiltInFunction("toState")

#######################################
# CONTEXT
#######################################

class Context:
    def __init__(self, display_name, parent=None, parent_entry_pos=None):
        self.display_name = display_name
        self.parent = parent
        self.parent_entry_pos = parent_entry_pos
        self.symbol_table = None

#######################################
# SYMBOL TABLE
#######################################

class SymbolTable:
    def __init__(self, parent=None):
        self.symbols = {}
        self.parent = parent

    def get(self, name):
        value = self.symbols.get(name, None)
        if value == None and self.parent:
            return self.parent.get(name)
        return value

    def set(self, name, value):
        self.symbols[name] = value

    def remove(self, name):
        del self.symbols[name]

#######################################
# INTERPRETER
#######################################

class Interpreter:
    def visit(self, node, context):
        method_name = f'visit_{type(node).__name__}'
        method = getattr(self, method_name, self.no_visit_method)
        return method(node, context)

    def no_visit_method(self, node, context):
        raise Exception(f'No visit_{type(node).__name__} method defined')

    ###################################

    def visit_NumberNode(self, node, context):
        return RTResult().success(
            Number(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_TextNode(self, node, context):
        return RTResult().success(
            Text(node.tok.value).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_ListNode(self, node, context):
        res = RTResult()
        elements = []

        for element_node in node.element_nodes:
            elements.append(res.register(self.visit(element_node, context)))
            if res.should_return(): return res  # Changed

        return res.success(
            List(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_VarAccessNode(self, node, context):
        res = RTResult()
        var_name = node.var_name_tok.value
        value = context.symbol_table.get(var_name)

        if not value:
            return res.failure(RTError(
                node.pos_start, node.pos_end,
                f"'{var_name}' is not defined",
                context
            ))

        # Special handling for Quit
        if isinstance(value, Quit):
            return res.success(value)

        value = value.copy()
        value.set_pos(node.pos_start, node.pos_end)
        value.set_context(context)
        return res.success(value)

    def visit_VarAssignNode(self, node, context):
        res = RTResult()
        var_name = node.var_name_tok.value
        value = res.register(self.visit(node.value_node, context))
        if res.error: return res

        context.symbol_table.set(var_name, value)
        return res.success(value)

    def visit_BinOpNode(self, node, context):
        res = RTResult()
        left = res.register(self.visit(node.left_node, context))
        if res.should_return(): return res  # Changed
        right = res.register(self.visit(node.right_node, context))
        if res.should_return(): return res  # Changed

        is_list = isinstance(left, List)

        # Addition operations
        if node.op_tok.type == TT_PLUS:
            result, error = left.added_to(right)
        elif node.op_tok.matches(TT_KEYWORD, 'plus'):
            if is_list:
                return res.failure(RTError(
                    node.pos_start, node.pos_end,
                    "Use 'add' or '+' for lists, not 'plus'",
                    context
                ))
            result, error = left.added_to(right)
        elif node.op_tok.matches(TT_KEYWORD, 'add'):
            if not is_list:
                return res.failure(RTError(
                    node.pos_start, node.pos_end,
                    "Use 'plus' or '+' for numbers, not 'add'",
                    context
                ))
            result, error = left.added_to(right)
        
        # Subtraction operations
        elif node.op_tok.type == TT_MINUS:
            result, error = left.subbed_by(right)
        elif node.op_tok.matches(TT_KEYWORD, 'minus'):
            if is_list:
                return res.failure(RTError(
                    node.pos_start, node.pos_end,
                    "Use 'remove' or '-' for lists, not 'minus'",
                    context
                ))
            result, error = left.subbed_by(right)
        elif node.op_tok.matches(TT_KEYWORD, 'remove'):
            if not is_list:
                return res.failure(RTError(
                    node.pos_start, node.pos_end,
                    "Use 'minus' or '-' for numbers, not 'remove'",
                    context
                ))
            result, error = left.subbed_by(right)
        
        # Multiplication operations
        elif node.op_tok.type == TT_MUL:
            result, error = left.timesed_by(right)
        elif node.op_tok.matches(TT_KEYWORD, 'times'):
            if is_list:
                return res.failure(RTError(
                    node.pos_start, node.pos_end,
                    "Use 'merge' or '*' for lists, not 'times'",
                    context
                ))
            result, error = left.timesed_by(right)
        elif node.op_tok.matches(TT_KEYWORD, 'merge'):
            if not is_list:
                return res.failure(RTError(
                    node.pos_start, node.pos_end,
                    "Use 'times' or '*' for numbers, not 'merge'",
                    context
                ))
            result, error = left.timesed_by(right)
        
        # Division operations
        elif node.op_tok.type == TT_DIV:
            result, error = left.dived_by(right)
        elif node.op_tok.matches(TT_KEYWORD, 'div'):
            if is_list:
                return res.failure(RTError(
                    node.pos_start, node.pos_end,
                    "Use 'get' or '/' for lists, not 'div'",
                    context
                ))
            result, error = left.dived_by(right)
        elif node.op_tok.matches(TT_KEYWORD, 'get'):
            if not is_list:
                return res.failure(RTError(
                    node.pos_start, node.pos_end,
                    "Use 'div' or '/' for numbers, not 'get'",
                    context
                ))
            result, error = left.dived_by(right)
        
        # Power operation
        elif node.op_tok.type == TT_POW or node.op_tok.matches(TT_KEYWORD, 'pow'):
            result, error = left.powed_by(right)
        
        # Comparison operations
        elif node.op_tok.type == TT_EE or node.op_tok.matches(TT_KEYWORD, 'is'):
            result, error = left.get_comparison_eq(right)
        elif node.op_tok.type == TT_NE or node.op_tok.matches(TT_KEYWORD, 'isnt'):
            result, error = left.get_comparison_ne(right)
        elif node.op_tok.type == TT_LT or node.op_tok.matches(TT_KEYWORD, 'under'):
            result, error = left.get_comparison_lt(right)
        elif node.op_tok.type == TT_GT or node.op_tok.matches(TT_KEYWORD, 'above'):
            result, error = left.get_comparison_gt(right)
        elif node.op_tok.type == TT_LTE or node.op_tok.matches(TT_KEYWORD, 'atmost'):
            result, error = left.get_comparison_lte(right)
        elif node.op_tok.type == TT_GTE or node.op_tok.matches(TT_KEYWORD, 'atleast'):
            result, error = left.get_comparison_gte(right)
        elif node.op_tok.matches(TT_KEYWORD, 'and'):
            result, error = left.anded_by(right)
        elif node.op_tok.matches(TT_KEYWORD, 'or'):
            result, error = left.ored_by(right)

        if error:
            return res.failure(error)
        else:
            return res.success(result.set_pos(node.pos_start, node.pos_end))

    def visit_UnaryOpNode(self, node, context):
        res = RTResult()
        number = res.register(self.visit(node.node, context))
        if res.error: return res

        error = None

        if node.op_tok.type == TT_MINUS:
            number, error = number.timesed_by(Number(-1))
        elif node.op_tok.matches(TT_KEYWORD, 'not'):
            number, error = number.notted()

        if error:
            return res.failure(error)
        else:
            return res.success(number.set_pos(node.pos_start, node.pos_end))

    def visit_IfNode(self, node, context):
        res = RTResult()

        for condition, expr, should_return_null in node.cases:
            condition_value = res.register(self.visit(condition, context))
            if res.error: return res

            if condition_value.is_true():
                expr_value = res.register(self.visit(expr, context))
                if res.should_return: return res
                return res.success(Number.null if should_return_null else expr_value)

        if node.otherwise_case:
            expr, should_return_null = node.otherwise_case
            otherwise_value = res.register(self.visit(expr, context))
            if res.should_return: return res
            return res.success(Number.null if should_return_null else otherwise_value)
        
        return res.success(Number.null)

    def visit_RepeatNode(self, node, context):
        res = RTResult()
        elements = []

        start_value = res.register(self.visit(node.start_value_node, context))
        if res.should_return(): return res  # Changed

        end_value = res.register(self.visit(node.end_value_node, context))
        if res.should_return(): return res  # Changed

        if node.step_value_node:
            step_value = res.register(self.visit(node.step_value_node, context))
            if res.should_return(): return res  # Changed
        else:
            step_value = Number(1) # otherwise step value

        i = start_value.value

        # yay inclusive
        if step_value.value >= 0:
            condition = lambda: i <= end_value.value
        else:
            condition = lambda: i >= end_value.value
        
        while condition():
            context.symbol_table.set(node.var_name_tok.value, Number(i))
            
            # Process the body, handling control statements as we encounter them
            value = res.register(self.visit(node.body_node, context))
            
            if res.loop_should_continue:
                res.loop_should_continue = False
                i += step_value.value
                continue
            
            if res.loop_should_break:
                res.loop_should_break = False
                break
            
            if res.should_return():
                return res
            
            if value and not (res.loop_should_continue or res.loop_should_break):
                elements.append(value)
            
            i += step_value.value

        return res.success(
            Number.null if node.should_return_null else
            List(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_WhileNode(self, node, context):
        res = RTResult()
        elements = []

        while True:
            condition = res.register(self.visit(node.condition_node, context))
            if res.should_return(): return res  # Changed

            if not condition.is_true(): break

            value = res.register(self.visit(node.body_node, context))
            if res.should_return() and res.loop_should_continue == False and res.loop_should_break == False: return res  # Changed

            if res.loop_should_continue:
                res.loop_should_continue = False
                continue

            if res.loop_should_break:
                res.loop_should_break = False
                break

            elements.append(value)

        return res.success(
            Number.null if node.should_return_null else
            List(elements).set_context(context).set_pos(node.pos_start, node.pos_end)
        )

    def visit_FuncDefNode(self, node, context):
        res = RTResult()

        func_name = node.var_name_tok.value if node.var_name_tok else None
        body_node = node.body_node
        arg_names = [arg_name.value for arg_name in node.arg_name_toks]
        func_value = Function(func_name, body_node, arg_names, node.should_auto_return).set_context(context).set_pos(node.pos_start, node.pos_end)

        if node.var_name_tok:
            context.symbol_table.set(func_name, func_value)

        return res.success(func_value)

    def visit_CallNode(self, node, context):
        res = RTResult()
        args = []

        value_to_call = res.register(self.visit(node.node_to_call, context))
        if res.should_return(): return res  # Changed
        value_to_call = value_to_call.copy().set_pos(node.pos_start, node.pos_end)

        for arg_node in node.arg_nodes:
            args.append(res.register(self.visit(arg_node, context)))
            if res.should_return(): return res  # Changed

        return_value = res.register(value_to_call.execute(args))
        if res.should_return(): return res  # Changed
        return_value = return_value.copy().set_pos(node.pos_start, node.pos_end).set_context(context)
        return res.success(return_value)
    
    def visit_GiveNode(self, node, context):
        res = RTResult()
        
        if node.node_to_return:
            value = res.register(self.visit(node.node_to_return, context))
            if res.should_return(): return res
        else:
            value = Number.null

        return res.success_return(value)

    def visit_NextNode(self, node, context):
        return RTResult().success_continue()
    
    def visit_StopNode(self, node, context):
        return RTResult().success_break()

#######################################
# QUIT / EXIT
#######################################

class Quit(Value):
    def __init__(self):
        super().__init__()
    
    def __call__(self, *args):
        return self

    def __repr__(self):
        return "<quit>"

    def copy(self):
        return self  # Return self since Quit is effectively a singleton

    def is_true(self):
        return True

#######################################
# RUN
#######################################

global_symbol_table = SymbolTable()
global_symbol_table.set("null", Number.null)
global_symbol_table.set("true", Number.true)
global_symbol_table.set("false", Number.false)
global_symbol_table.set("quit", Quit())
global_symbol_table.set("math_pi", Number.math_PI)
global_symbol_table.set("say", BuiltInFunction.say)
global_symbol_table.set("saySave", BuiltInFunction.saySave)
global_symbol_table.set("ask", BuiltInFunction.ask)
global_symbol_table.set("askNumber", BuiltInFunction.askNumber)
global_symbol_table.set("clean", BuiltInFunction.clean)
global_symbol_table.set("clear", BuiltInFunction.clean)
global_symbol_table.set("cls", BuiltInFunction.clean)
global_symbol_table.set("isNumber", BuiltInFunction.isNumber)
global_symbol_table.set("isText", BuiltInFunction.isText)
global_symbol_table.set("isList", BuiltInFunction.isList)
global_symbol_table.set("isFunction", BuiltInFunction.isFunction)
global_symbol_table.set("append", BuiltInFunction.append)
global_symbol_table.set("pop", BuiltInFunction.pop)
global_symbol_table.set("extend", BuiltInFunction.extend)
global_symbol_table.set("lengthOf", BuiltInFunction.lengthOf)
global_symbol_table.set("run", BuiltInFunction.run)
# global_symbol_table.set("random", BuiltInFunction.random)
global_symbol_table.set("exit", Quit())
global_symbol_table.set("typeOf", BuiltInFunction.typeOf)
global_symbol_table.set("toNum", BuiltInFunction.toNumber)
global_symbol_table.set("toText", BuiltInFunction.toText)
global_symbol_table.set("toList", BuiltInFunction.toList)
global_symbol_table.set("toState", BuiltInFunction.toState)

def run(fn, text):
    # Generate tokens
    lexer = Lexer(fn, text)
    tokens, error = lexer.make_tokens()
    if error: return None, error
    
    # Generate AST
    parser = Parser(tokens)
    ast = parser.parse()
    if ast.error: return None, ast.error

    # Run program
    interpreter = Interpreter()
    context = Context('<program>')
    context.symbol_table = global_symbol_table
    result = interpreter.visit(ast.node, context)

    return result.value, result.error


# TEST CASES
if __name__ == "__main__":
    print("Testing expressions:")
    print()
    
    # Test 1: 1 plus 1
    print("Test 1: 1 plus 1")
    result, error = run('<test>', '1 plus 1')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()
    
    # Test 2: 1 add 1
    print("Test 2: 1 add 1")
    result, error = run('<test>', '1 add 1')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()
    
    # Test 3: [1] plus 2
    print("Test 3: [1] plus 2")
    result, error = run('<test>', '[1] plus 2')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()
    
    # Test 4: [1] add 2
    print("Test 4: [1] add 2")
    result, error = run('<test>', '[1] add 2')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()
    
    # Additional tests
    print("Additional tests:")
    print()
    
    # Test 5: [1, 2] + 3
    print("Test 5: [1, 2] + 3")
    result, error = run('<test>', '[1, 2] + 3')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()
    
    # Test 6: [1, 2] minus 0
    print("Test 6: [1, 2] minus 0")
    result, error = run('<test>', '[1, 2] minus 0')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()
    
    # Test 7: [1, 2] remove 0
    print("Test 7: [1, 2] remove 0")
    result, error = run('<test>', '[1, 2] remove 0')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()
    
    # Test 8: [1, 2] times [3, 4]
    print("Test 8: [1, 2] times [3, 4]")
    result, error = run('<test>', '[1, 2] times [3, 4]')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()
    
    # Test 9: [1, 2] merge [3, 4]
    print("Test 9: [1, 2] merge [3, 4]")
    result, error = run('<test>', '[1, 2] merge [3, 4]')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()

    print("Test 10: say(\"What's your favorite number?\"). set n to askNumber()")
    result, error = run('<test>', 'say("What\'s your favorite number?"). set n to askNumber()')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()

    print("Test 11: say(\"What's your favorite number?\"). set n to askNumber(). if n above 10 then say(\"That's a big number!\") otherwise say(\"That's a small number!\"). say(n)")
    result, error = run('<test>', 'say("What\'s your favorite number?"). set n to askNumber(). if n above 10 then say("That\'s a big number!") otherwise say("That\'s a small number!"). say(n)')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()

    print("Test 12: Counting from 1 to 5")
    result, error = run('<test>', 'repeat i from 1 through 5 do say(i)')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()

    print("Test 13: Quitting the program")
    result, error = run('<test>', 'quit')
    if error:
        print(f"ERROR: {error.as_string()}")
    else:
        print(f"Result: {result}")
    print()

    print("All tests completed.")