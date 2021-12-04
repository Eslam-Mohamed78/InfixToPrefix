# InfixToPrefix
infix to prefix and prefix evaluator

## To run that program 

Step 1: got to evaluator.py file and run it 

Step 2: write in the console the infix expression => "that u want to convert it to prefix exp and evaluate it"

You will have the prefix exp and the result of it.

## Let's explain what the program consist of:

### First: InfixToPrefix Program

This program takes one argument which is the infix expression and convert it to prefix expression,

And this program algorithm depends on the infixToPostfix algorithm but with some changes as follows: 

Step 1: Reverse the infix expression i.e A+B*C will become C*B+A. Note while reversing each ‘(‘ will become ‘)’ and each ‘)’ becomes ‘(‘.

Step 2: Obtain the “nearly” postfix expression of the modified expression i.e CB*A+.

Step 3: Reverse the expression. Hence in our example prefix is +A*BC.

Note that for Step 2, we don’t use the postfix algorithm as it is. 

There is a minor change in the algorithm.

we have to pop all the operators from the stack which are greater than or equal to in precedence than that of the scanned operator.

But here, we have to pop all the operators from the stack which are greater in precedence than that of the scanned operator.

Only in the case of “^” operator, we pop operators from the stack which are greater than or equal to in precedence.


### Second: Prefix Evaluator

ويقوم باخراج ناتج هذه العملية الحسابية و الجوريزم هذا البرنامج هو كالاتي  prefix هذا البرنامج ياخذ متغير واحد في صيغة

Step 1: Reverse the prefix expression.

Step 2: if the token was operand => push to the stack 
        if the token was operator => pop from stack so the value will be the first operand
                                     then pop again from the stack so the value will be the secon operand (Unlike postfix evaluator) 
       
Step 3: doMath function تقوم بتنفيذ العملية الحسابية علي المتغيران والعلامة اللي هتاخذهم







