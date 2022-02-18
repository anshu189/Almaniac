'''
Script Written By: Anshu Saini
Copyright: Anshu Saini
Github: https://github.com/anshu189
Application: Almaniac.exe
Platforms: Windows/Mac/Linux

'''

# <----- Packages Used ----->

import os
import wget
from art import *
import webbrowser as wb
from time import sleep as s
from rich.console import Console
from rich.table import Table
from rich.syntax import Syntax
from rich.markdown import Markdown
from termcolor import colored as colo
import pygments.lexers.c_cpp

# <----- Assets ----->

os.system("cls")
os.system("title Almaniac - The C Guidance")
os.system("color 07")
dim_yellow = "#e9eb9d"
crimson_red = "#FF1919"
greenish_sky = "#21BF70"
console_theme = "monokai"
console = Console()


def contentmenu():
    content = '''
    1. Introduction to C Programming Language.
    2. How to install and setup VsCode for C/C++ compiler Language. (Video Explanation + Blog)
    3. How to use console for compiling the C Programmes.
    4. What is Flwochat/Algorithm? (Video Explanation + Blog)
    5. Overview to Structure of a C Programme code.
    6. Starter Hello World Programme code.
    7. Input/Output Functions with Programme code.
    8. Format Sepcifiers with Programme code.
    9. Data Types with Programme code.
    10. Types of Operators in C with Programme code.
    11. Implicit/Explicit Type Casting Programme code.
    12. Decision Control Statements Programme code.
    13. Switch Statement Programme code.
    14. Conditional operator and GOTO Programme code.
    15. Looping Statements with Programme code.
    16. Nested Loops Programme code.
    17. Jump Statement Programme code.
    18. Declaration & Initialization of Arrays Programme code.
    19. One & Two Dimentional Arrays with Programme code.
    20. Searching & Sorting through Arrays Programme code.
    21. Intro. to Strings with Programme code.
    22. Intro. to Functions with Programme code (Declaration & Initialization).
    23. User Defined Functions Programme code.
    24. Recurssive Functions Programme code.
    25. Intro. to Macros in C.
    26. Basics of Pointers with Programme code.
    27. Pointer to Pointer, Pointer Programme code.
    28. Pointer to Array Programme code.
    29. Pointer with Functions Programme code.
    30. Intro. to Storage Classes with Programme code.
    31. Basics of Structure in C with Programme code.
    32. Nested & Array of Structure with Programme code.
    33. Using Structure with Function Programme code.
    34. Basics of DMA (Dynamic Memory Allocation).
    35. DMA to Array & Structures with Programme code.
    69. Not Basic Programme with Basics.
    99. CheatSheet Worksheet >:)
    77. About Me ¯\_(^_-)_/¯
    00. Shh
        '''
    console.print(" Content: ", style="white on magenta")
    console.print(content, style="cyan")


def welcome():
    user_name = input("Heya mate! Your good name? ")
    os.system("cls")
    Art=text2art("Welcome To Almaniac")
    print(colo("------------------------------------------------------------\
------------------------------------------------------------", "magenta"))
    print(colo(Art, "cyan"))
    print(colo("------------------------------------------------------- By 4n5hu \
-------------------------------------------------------", "magenta"))

    console.print(f" -------------{len(user_name)*'-'}", style=greenish_sky)
    console.print(f"| {user_name} Logged in! |", style=f'black on {greenish_sky}')
    console.print(f" -------------{len(user_name)*'-'}\n\n", style=greenish_sky)
    contentmenu()


def C_intro_1(): 
    introc = '''
 ► C is a procedural programming language. 
 ► It was initially developed by Dennis Ritchie in the year 1972.
 ► It was mainly developed as a system programming language to write an operating system. 
 ► The main features of the C language
	• It include low-level memory access 
	• A simple set of keywords
	• Clean style 
 ► These features make C language suitable for system programmings like an operating system or compiler development.
'''
    print("\n")
    print(colo("-------------------------------------------------------------\
----------------------------------------------------------", "magenta"))
    console.print("Introduction to C Programming Langage:", style="cyan")
    console.print(introc, style=dim_yellow)
    print(colo("-------------------------------------------------------------\
---------------------------------------------------------", "magenta"))
    print("\n")


def C_install_2():

    def installchoice():
        doc = "1. Download VsCode for Windows(7,8,10 & 11)\
            \n2. Download VsCode for Linux\
            \n3. Download VsCode for Mac (Zipped File)\
            \n4. Exit"
        print(colo("\n--------------------------------------------", "magenta"))
        console.print(doc, style=dim_yellow)
        print(colo("\n--------------------------------------------", "magenta"))
        print("\n")

        def installchoice2():
            try:
                installchoice = int(input("Please Choose any > "))
                print("\n")
                if installchoice == 1:
                    print(colo("--------------------------------------------", "blue"))
                    print("Steps to install Vscode:\n1. Check I Agree the agreement and hit Next\
                        \n2. Choose your installation location or leave it default then Click Next\
                        \n3. Click Next\
                        \n4. Check the box *Add to PATH* (Important) then Click Next\
                        \n5. Click Install\n6. Click Finish\n7. You are now set with VsCode!")    
                    print(colo("--------------------------------------------", "blue"))
                    s(1)
                    wb.open_new_tab("https://code.visualstudio.com/sha/download?build=stable&os=win32-x64-user")
                    
                    def installcompiler():
                        try:
                            print("\n")
                            compilerinstall = input("Do you want to install and setup C Compiler? (yes or no) > ")
                            print("\n")
                            if compilerinstall == "yes" or compilerinstall == "Yes":
                                print(colo("--------------------------------------------", "blue"))
                                print("Steps to setup C/C++ compiler:\
                                    \n1. Click on Install\
                                    \n2. Click Continue\
                                    \n3. Wait for to fininsh the download...\
                                    \n4. Click Continue when finished\
                                    \n5. Right click on *minngw32-base*, *minngw32-gcc-g++* & *minngw32-gcc-objc* and Mark for Installation\n6. Under Installation tab Click *Apply Change*\
                                    \n7. Click Apply...\
                                    \n8. Wait for it to finish the installation then Click Close(all window)\n")
                                console.print("------------------Important Procdeure------------------", style=crimson_red)
                                print("Steps to add mingw bin to Environmental PATH Variables:\
                                    \n1. Navigate to *Local Disk (C:)*\
                                    \n2. Open MinnGW > bin\
                                    \n3. Hit *Alt + D* then *Ctrl + C*\
                                    \n4. Now press *Win + R* paste this *rundll32.exe sysdm.cpl,EditEnvironmentVariables* hit *Ctrl + Shift + Enter*\n5. Under System Variables Click on *PATH* then Click on Edit\
                                    \n6. Click New and Paste the Path you copied in *step 2 & 3*\
                                    \n7. Click OK then OK again\
                                    \n8. Open VsCode Click on Extensions Tab from the left sidebar\
                                    \n9. Search C/C++ and Code Runner install both of them\
                                    \n10. After installation open VsCode Settings\
                                    \n11. Search Code Runner and Check the box of *Code-Runner: Run In Terminal* & *Code-Runner: Save File Before Run*\n12. Voalá! You are all set now!")
                                print(colo("Ahhh... It's easy right? xD", "green"))
                                print(colo("--------------------------------------------\n", "blue"))
                                s(1)
                                wb.open_new_tab("https://sourceforge.net/projects/mingw/files/latest/download")
                            elif compilerinstall == "no" or compilerinstall == "No":
                                pass
                            else:
                                print("Invalid Input! Try Again.\n")
                                installcompiler()
                        except:
                            installcompiler()
                    installcompiler()

                elif installchoice == 2:
                    wb.open_new_tab("https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64")
                elif installchoice == 3:
                    wb.open_new_tab("https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal")
                elif installchoice == 4:
                    choice_by_user()
                else:
                    print("Invalid Input! Try Again.\n")
                    installchoice2()
            except:
                installchoice2()
        installchoice2()
    installchoice()


def C_use_compile_3():
    how_t_compile = '''► **gcc hello.c** or **gcc hello.c -o 'name_of_your_outputfile'** (-o is optional) [Command to compile the code]
► **./a.exe**  [Execute the above compiled file]
► Hello, World!
'''
    md = Markdown(how_t_compile)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("How to compile & Execute a C programme", style="cyan")
    console.print(md, style=dim_yellow)
    print(colo("--------------------------------------------", "magenta"))
    print("\n")


def algorithm_flowchart_4():    
    def alog_selection():
        try:
            print(colo("\n--------------------------------------------", "magenta"))
            quicknotes = '''Here you go!
    Step 1 : Start
    Step 2 : Input a, b, c
    Step 3 : if a > b goto step 4, otherwise goto step 5
    Step 4 : if a > c goto step 6, otherwise goto step 8
    Step 5 : if b > c goto step 7, otherwise goto step 8
    Step 6 : Output "a is the largest", goto step 9
    Step 7 : Output "b is the largest", goto step 9
    Step 8 : Output " c is the largest", goto step 9
    Step 9 : Stop'''
            print("1. Youtube Video Explanation + Blog Article\
                \n2. Quick Notes\
                \n3. Both\
                \n4. Exit")
            print(colo("--------------------------------------------", "magenta"))
            algochoice = int(input("\nPlease select any or both option > "))
            if algochoice == 1:
                wb.open_new_tab("https://www.javatpoint.com/flowchart-in-c-programming-language")
                wb.open_new_tab("https://youtu.be/1p0uMbY4w8A")
                alog_selection()
            elif algochoice == 2:
                console.print("How to write an Algorithm?", style="cyan")
                console.print(quicknotes, style=dim_yellow)
                alog_selection()
            elif algochoice == 3:
                console.print(quicknotes, style=dim_yellow)
                s(1)
                wb.open_new_tab("https://www.javatpoint.com/flowchart-in-c-programming-language")
                wb.open_new_tab("https://youtu.be/1p0uMbY4w8A")
                alog_selection()
            elif algochoice == 4:
                choice_by_user()
            else:
                print("Invalid Input! Try Again.\n")
                alog_selection()
        except:
            alog_selection()
    alog_selection()
    print("\n")


def C_structure_5(): 
    table = Table(title="Basic Structure of C Programme", show_header=True)
    table.add_column("Header Files Inclusion", style="dim", width=18)
    table.add_column("Main Method (function) Declaration")
    table.add_column("Variable Declaration", width=18)
    table.add_column("Main Body", width=18)
    table.add_column("Return Statement", width=18)

    table.add_row("[cyan]#include <stdio.h>[/cyan]",
        "[cyan]int main() {\n}[/cyan]",
        "[cyan]int main() {\n\tint a;\n}[/cyan]",
        "[cyan]int main() {\n\tint a;\n\tprintf('%d', a);\n}[/cyan]",
        "[cyan]int main() {\n\tint a;\n\tprintf('%d', a);\n\treturn 0;\n}[/cyan]")

    print("\n")
    console.print(table)
    print("\n")


def startr_temp_6():
    startertemplate = '''#include <stdio.h>
int main() {
    // my first program in C
    printf("Hello, World!");
    return 0;
}'''
    templatecode = Syntax(startertemplate, "C", theme=console_theme, line_numbers=True)

    print(colo("\n--------------------------------------------", "magenta"))
    console.print("Hello World Programme Template\n", style="cyan")
    console.print(templatecode)
    print("\n")
    console.print("► Note: We implement Single Line Comments in C using “//\
  This is a single line comment”\nFor Multiline Comments “/* This is a multi-line comment*/” (Ignore double quotes)", style=dim_yellow)
    print(colo("--------------------------------------------\n", "magenta"))


def i_o_func_7(): 
    notes= '''• Un-formatted I/O
    o getch() -- Reads a single character form the user at console without returning it.
    o getche() -- Reads a single character form the user at console and returning it.
    o getchar() -- Reads a single character form the user at console and returning it only when pressed ENTER Key.
    o gets() -- Reads a single string form the user at console and returns only when pressed ENTER Key.

• Formatted I/O
    o scanf() -- Formatted input function used to read one or many inputs from the standard keyboard device..
    o printf() -- Formatted output function used to print one or many values out to the console.
    o sscanf() -- Formatted input function used to read one or many reads formatted input from a string.from
    o printf() -- Formatted output function used to print one or many formatted output to a string pointed to, by str.
'''
    programmecode = '''#include <stdio.h>
int main() {

    char name[30];                                            
    int roll;                                                               
    char grade;                                   

   // Uncomment any of the apporach and execute the programme.

   // Approach 1: Using scanf() functions we can only take input untill there's a whitespaces.
      scanf("Name, Roll no. & Grade: %s %d %c", name, &roll, &grade); 

   // Approach 2: Here gets() functions is used to get the surname too, means taking input after the whitespaces.
 /* puts("Name:");
    gets(name);
    printf("Roll no.: ");
    scanf("%d", &roll);
    puts("Grade:");
    scanf("%c",grade); */

    printf("Name: %s", name);  
    printf("Roll No.: %d", roll);            
    puts("Grade");
    printf("%c", grade);                
    return 0;                                         
}'''
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nINPUT AND OUTPUT FUNCTIONS IN C\n", style="cyan")
                console.print(notes, style=dim_yellow)
                i_o_func()
            elif i_ochoice==2:
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def format_specifier_8(): 
    fs_notes = '''► %d -- Used to read or print Integers
► %c -- Used to read or print Characters
► %s -- Used to read or print String
► %f -- Used to read or print Floating Integers
► %u -- Used to read or print Unsigned Integers
► %lu -- Used to read or print Unsigned Long Variables
► %ld -- Used to read or print Signed Long Variables
► %lf -- Used to read or print Double floating integers
► %Lf -- Used to read or print Long Double floating integers'''
    programmecode = '''#include <stdio.h>
int main() {
   int x;
   float y;
   char z;
   scanf("%3d %4f %c", &x, &y, &z);
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def f_s_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nFormat Specifiers in C\n", style="cyan")
                console.print(fs_notes, style=dim_yellow)
                f_s_func()
            elif i_ochoice==2:
                console.print(templatecode)
                f_s_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                f_s_func()
        except:
            f_s_func()
    f_s_func()


def data_types_9(): 
    table = Table(title="Data Types in C", show_header=True)
    table.add_column("Primary", style="dim", width=18)
    table.add_column("Derived")
    table.add_column("User Defined", width=18)

    table.add_row("[cyan]Integer[/cyan]",
        "[cyan]Function[/cyan]",
        "[cyan]Class[/cyan]")
    table.add_row("[cyan]Character[/cyan]",
        "[cyan]Array[/cyan]",
        "[cyan]Structure[/cyan]")
    table.add_row("[cyan]Boolean[/cyan]",
        "[cyan]Pointer[/cyan]",
        "[cyan]Union[/cyan]")
    table.add_row("[cyan]Floating Point[/cyan]",
        "[cyan]Reference[/cyan]",
        "[cyan]Enum[/cyan]")
    table.add_row("[cyan]Double Floating Point[/cyan]","",
        "[cyan]Typedef[/cyan]")
    table.add_row("[cyan]Void[/cyan]","","")
    table.add_row("[cyan]Wide Character[/cyan]","","")
    
    programmecode = '''#include <stdio.h>

int main() {

    char name[30];  // Declaration of Character name with size of 30
    int hue;  // Declaration of int hue
    char you;  // Declaration of Character you
    float cheems;  // Declaration of float cheems
    int array[30] = {0,96,69};  //Declaration & Initialization of int array of max size 30 elements                                              
    int *ahh;  // Declaration of Pointer *ahh [Astrics(*) sign is important]
    int this_is_used_defined_functions();  // User Defined Function

    gets(name);  // gets() func. takes input with Whitspaces
    scanf("%d", &hue);  // Ampersand(&) Sign is important for int & float DataTypes to store the value in it
    scanf(" %c", &you);
    scanf("%f", &cheems);

    printf("%s", name);
    printf("%d", hue);
    printf("%c", you);
    printf("%f", cheems);
    printf("%p", ahh); // %p is used for pointer location value [null]
    return 0;                                         
}'''
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def d_t_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print(table)
                d_t_func()
            elif i_ochoice==2:
                console.print(templatecode)
                d_t_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                d_t_func()
        except:
            d_t_func()
    d_t_func()


def operators_10(): 
    opr_notes = '''► Arithmetic Operators -- [ +, -, *, /, % ] 
► Relational Operators -- [ >, <, >=, <=, ==, != ]
► Logical Operators -- [ &&, ||, ! ]
► Assignment Operators -- [ =, +=, -=, *=, /=, %= ]
► Increment/decrement Operators -- [ ++, -- ]
► Conditional Operators (Ternary operators) -- [ ?: > 1==1? Yes: No;  (If 1==1 condition is True then return “Yes” else return “No”) ] 
► Bitwise Operators -- [ &, |, ^, <<, >>, ~ ]
► Special Operators -- [ sizeof(), (,) comma separator operator, (*) pointer operation, (&) ampersand, (. and ->) selection operator ]'''
    
    programmecode = '''<----- Arithmetic Operators Programme Code ----->

#include<stdio.h>
int main() {
   int a,b;
   printf("Input the value of a and b: ");
   scanf("%d %d",&a, &b);                  //Input the value of a and b
   printf("Result of a+b is: %d",a+b);   //Addition of a and b
   printf("Result of a-b is: %d",a-b);   //Subtraction of and b 
   printf("Result of a*b is: %d",a*b);   //Multiplication of a and b
   printf("Result of a/b is: %d",a/b);   // Division of a and b
   printf("Result of a%b is: %d",a%b);   //Remainder of division of a and b
   return 0;
}

<----- Relational Operators Programme Code ----->

#include <stdio.h>
int main() {
   int a,b,c;
   printf("Input the value of a,b & c: ");
   scanf("%d %d %d",&a, &b, &c);
  printf("%d == %d is %d", a, b, a == b);
   printf("%d == %d is %d", a, c, a == c);
   printf("%d > %d is %d", a, b, a > b);
   printf("%d > %d is %d", a, c, a > c);
   printf("%d < %d is %d", a, b, a < b);
   printf("%d < %d is %d", a, c, a < c);
   printf("%d != %d is %d", a, b, a != b);
   printf("%d != %d is %d", a, c, a != c);
   printf("%d >= %d is %d", a, b, a >= b);
   printf("%d >= %d is %d", a, c, a >= c);
   printf("%d <= %d is %d", a, b, a <= b);
   printf("%d <= %d is %d", a, c, a <= c);
   return 0;
}

<----- Logical Operators Programme Code ----->

#include <stdio.h>
int main() {
   int a, b, c, result;
   printf("Input the value of a, b & c: ");
   scanf("%d %d %d",&a,&b, &c);
   result = (a == b) && (c > b);
   printf("(a == b) && (c > b) is %d", result);
   result = (a == b) && (c < b);
   printf("(a == b) && (c < b) is %d", result);
   result = (a == b) || (c < b);
   printf("(a == b) || (c < b) is %d", result);
   result = (a != b) || (c < b);
   printf("(a != b) || (c < b) is %d", result);
   result = !(a != b);
   printf("!(a == b) is %d", result);
   result = !(a == b);
   printf("!(a == b) is %d", result);
   return 0;
}

<----- Assignment Operators Programme Code ----->

#include <stdio.h>
int main() {
   int a, c;
   printf("Input the value of a: ");
   scanf("%d", &a);
   c = a;
   printf("c =: %d", c);
   c += a;
   printf("c +=:  %d", c);
   c -= a;
   printf("c -=:  %d", c);
   c *= a;
   printf("c *=: %d", c);
   c /= a;
   printf("c /=: %d", c);
   c %= a;
   printf("c %=: %d", c);
   return 0;
}

<----- Increment and Decrement Operators Programme Code ----->

#include <stdio.h>
int main() {
   int a, b;
   printf("Input the value of a & b: ");
   scanf("%d %d",&a, &b);
   printf("++a = %d", ++a);  // Pre-Increment
   printf("--b = %d", --b);  // Pre-Decrement
   printf("a++ = %d", a++);  // Post-Increment
   printf("b-- = %d", b--);  // Post-Decrement
   return 0;
}

<----- Assignment Operators Programme Code ----->

#include <stdio.h>
#include <stdlib.h>
int main() {
int year;
printf("Input a year to check if it's a leap year or not: ");
scanf("%d", &year);
   (year%4==0 && year%100!=0) ? printf("It's a Leap Year") :
       (year%400 ==0 ) ? printf("It's a Leap Year") : printf("It's not a Leap Year");
 }

<----- Bitwise Operators Programme Code (For Binary digits '0's & '1's only) ----->

#include <stdio.h>
int main()
{
   unsigned char a = 5, b = 9;
   printf("a = %d, b = %d", a, b);
   printf("a&b (AND) = %d", a & b);
   printf("a|b (OR) = %d", a | b);
   printf("a^b (XOR) = %d", a ^ b);
   printf("~a (COMPLEMENT) = %d", a = ~a);
   printf("b<<1 (LEFT SHIFT) = %d", b << 1);
   printf("b>>1 (RIGHT SHIFT) = %d", b >> 1);
   return 0;
}

<----- Other Special Operators Programme Code ----->

#include <stdio.h>
int main() {
   int a, z, y; // Declaration of a, z & y
   z = 3,7;  // Initialization of z 
   y = (6,2,8,9);  // Initialization of y  
   float b;
   double c;
   char d;
   printf("Size of int: %lu bytes", sizeof(a));
   printf("Size of float: %lu bytes", sizeof(b));
   printf("Size of double: %lu bytes", sizeof(c));
   printf("Size of char: %lu byte", sizeof(d));
   printf("Value of z is: %d", z);
   printf("Value of y is: %d", y);
   return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def opr_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nOperators in C\n", style="cyan")
                console.print(opr_notes, style=dim_yellow)
                opr_func()
            elif i_ochoice==2:
                console.print(templatecode)
                opr_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                opr_func()
        except:
            opr_func()
    opr_func()


def type_casting_11():
    programmecode = '''#include<stdio.h>
int main(){

    // Implicit -- Lower to Higher Data Type
    char ch='a';
    int a = 13;
    printf("%d",a + ch);
    
    // Explicit -- Higher to Lower Data Type
    double db = 4.6;
    double dc = 4.9;
    double da = 4.5;
    int result = (int)da + (int)db + (int)dc;
    printf("%d", result);
    return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Programme Code\n2. Exit", style=dim_yellow)
    def t_c_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nType Casting in C\n", style="cyan")
                console.print(templatecode)
                t_c_func()
            elif i_ochoice==2:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                t_c_func()
        except:
            t_c_func()
    t_c_func()


def decision_statement_12(): 
    programmecode = '''<----- Template ----->
    
    if (condition x) {
        // The statements present inside the body of if
    }
    else {
        // The statements present inside the body of else
    }

#include <stdio.h>

int main() {

    int year;
    printf("Enter a year to check if it is a leap year or not: ");
    scanf("%d", &year);
    
    if(year%400 == 0) 
        printf("%d is a leap year.", year);
    else if(year%100 == 0) 
        printf("%d isn't a leap year.", year);
    else if(year%4 == 0) 
        printf("%d is a leap year.", year);
    else 
        printf("%d isn't a leap year.", year);
    
    return 0;
}

<-------------------- OR -------------------->

#include <stdio.h>

int main() {
    int year;
    printf("Input any year: ");
    scanf("%d", &year);

    if((year % 4 == 0) && ((year % 100 != 0) || (year % 400 == 0))) {
        printf("Yep, The provided year is a leap year!");
    }
    else{
        printf("Nope, The provided year is not a leap year.");
    }
    return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Programme Code\n2. Exit", style=dim_yellow)
    def d_s_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nDecision Statements in C\n", style="cyan")
                console.print(templatecode)
                d_s_func()
            elif i_ochoice==2:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                d_s_func()
        except:
            d_s_func()
    d_s_func()


def switch_13(): 
    programmecode = '''<----- Template ----->
    
switch(expression) {

   case constant-expression :
      statement(s);
      break; // optional
	
   case constant-expression:
      statement(s);
      break; // optional
  
   /* you can have any number of case statements */
   default : // Optional
   statement(s);
}

#include <stdio.h>

int main() {
    int a = 4;
    switch(a) {
    case 1:
        printf("I am One");
        break;
    case 2:
        printf("I am Two");
        break;
    case 3:
        printf("I an Three");
        break;
    case 4:
        printf("I am Four");
        break;
    case 5:
        printf("I am Five");
        break;
    default:
        printf("I am default");
    }
    return 0;
}

<-------------------- OR -------------------->

#include <stdio.h>
 
int main () {
   char grade = 'B';

   switch(grade) {
      case 'A':
        printf("Excellent!" );
        break;
      case 'B':
      case 'C':
        printf("Well done" );
        break;
      case 'D':
        printf("You passed" );
        break;
      case 'F':
        printf("Better try again" );
        break;
      default:
        printf("Invalid grade" );
    }
   printf("Your grade is %c", grade);
 
   return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Programme Code\n2. Exit", style=dim_yellow)
    def t_c_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nSwitch in C\n", style="cyan")
                console.print(templatecode)
                t_c_func()
            elif i_ochoice==2:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                t_c_func()
        except:
            t_c_func()
    t_c_func()


def conditional_14(): 
    programmecode = '''<----- Template ----->
variable = Expression1 ? Expression2 : Expression3;

#include <stdio.h>
  
int main() {  
    int age;  
    printf("Input your age: ");  
    scanf("%d", &age);  
    // If your age is greater than or equal to 18 then Expression2 will be executed otherwise Expression3 will execute.
    (age>=18)? (printf("You are eligible for voting")) : (printf("You are not eligible for voting"));  
    return 0;  
}  

<-------------------- OR -------------------->
 
#include <stdio.h>

int main() {  
    int a=5, b;  
    b = ((a==5) ? (3) : (2));  
    printf("The value of 'b' variable is: %d", b);  
    return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Programme Code\n2. Exit", style=dim_yellow)
    def t_c_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nConditional Operators in C\n", style="cyan")
                console.print(templatecode)
                t_c_func()
            elif i_ochoice==2:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                t_c_func()
        except:
            t_c_func()
    t_c_func()


def looping_15(): 
    table = Table(title="Looping Statements in C", show_header=True)
    table.add_column("for Loop (Entry Controlled)")
    table.add_column("while Loop (Entry Controlled)")
    table.add_column("do-while Loop (Exit Controlled)")

    table.add_row("[cyan]A for loop is a repetition control structure that allows you to efficiently write a loop that needs to execute a specific number of times.[/cyan]",
        "[cyan]Repeats a statement or group of statements untill a given condition is true. It tests the condition before executing the loop body.[/cyan]",
        "[cyan]A do-while loop is similar to a while loop, except the fact that it is guaranteed to execute at least once irrespective of test condition.[/cyan]")
    
    programmecode = '''<----- Template ----->
For Loop:
    for(initialization; condition; increment/decrement) {
        statement(s);
    }
While Loop:
    while(condition) {
        statement(s);
    }
Do-While Loop:
    do {
        statement(s);
    } 
    while(condition);

<-------------------- For Loop -------------------->

#include <stdio.h>
 
int main() {
    int a;
    for(a = 10; a < 21; a = a + 1){
        printf("Value of a: %d", a);
    }
   return 0;
}  

<-------------------- OR -------------------->
 
#include <stdio.h>
 
int main() {
    for(int a = 10; a < 21; a++){
        printf("Value of a: %d", a);
    }
   return 0;
}  

<-------------------- While Loop -------------------->

#include <stdio.h>
 
int main() {
    int a = 10;
    while(a < 21) {
        printf("Value of a: %d", a);
        a++;
    }
   return 0;
}

<-------------------- Do-While Loop -------------------->
 
#include <stdio.h>
 
int main() {
    int a = 10;
    do {
        printf("Value of a: %d", a);
        a = a + 1; // or a++; or a+=1;
   }
   while(a < 21);
   return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def d_t_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print(table)
                d_t_func()
            elif i_ochoice==2:
                console.print("\nLoops in C\n", style="cyan")
                console.print(templatecode)
                d_t_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                d_t_func()
        except:
            d_t_func()
    d_t_func()


def loop_nested_16(): 
    programmecode = '''<----- Template ----->
For Loop:
    for(initialization; condition; increment/decrement) {
        for(initialization; condition; increment/decrement) {
            statement(s);
        }
    statement(s);
    }
While Loop:
    while(condition) {
        while(condition) {
            statement(s);
        }
    statement(s);
    }
Do-While Loop:
    do {
        statement(s);
        do {
            statement(s);
        }
        while(condition);
    }
    while(condition);

<-------------------- For Nested Loop -------------------->

#include <stdio.h>  

int main() {  
    int n;
    printf("Input the value of n: ");  

    for(int i=1;i<=n;i++) { // outer loop  
        for(int j=1;j<=10;j++) { // inner loop  
            printf("%d ",(i*j)); // printing the value.  
        }  
        printf("\n");
    }
    return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Programme Code\n2. Exit", style=dim_yellow)
    def t_c_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nNested Loops in C\n", style="cyan")
                console.print(templatecode)
                t_c_func()
            elif i_ochoice==2:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                t_c_func()
        except:
            t_c_func()
    t_c_func()


def jump_statement_17(): 
    programmecode = '''<----- Template ----->
    
GOTO:
    goto label;
    . // Your code goes here
    ..
    label:
    statement;

<-------------------- GOTO -------------------->

#include <stdio.h>
 
int main() {
    int n = 1;
    label:
    printf("%d ", n);
    n++;

    if(n<=10)
        goto label;
   
   return 0;
}

<-------------------- Continue -------------------->

#include<stdio.h>

int main() {
    int i;
    for(i=1; i<=5; i++){
        if(i==2)
        continue;
        printf("%d", i);
    }
    return 0;
}

<-------------------- Break -------------------->

#include<stdio.h>

int main(){
    int i;
    for(i=1; i<=5; i++){
        printf ("%d", i);
        if (i==3)
        break;
    }
    return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Programme Code\n2. Exit", style=dim_yellow)
    def t_c_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nJump Statements in C\n", style="cyan")
                console.print(templatecode)
                t_c_func()
            elif i_ochoice==2:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                t_c_func()
        except:
            t_c_func()
    t_c_func()


def arrays_declare_initialize_18(): 
    notes= '''► An array is defined as the collection of similar type of data items stored at contiguous memory locations & can store data types such as int, char, double, float, etc.

► Array is the simplest data structure where each data element can be randomly accessed by using its index number.
'''
    table = Table(title="Arrays in C", show_header=True)
    table.add_column("Declaration")
    table.add_column("Initialization")
    table.add_column("Declaration & Initialization")

    table.add_row("[cyan]data_type array_name[array_size];\nint omkey[5];[/cyan]",
        "[cyan]omkey[0]=80;\nomkey[1]=12;[/cyan]",
        "[cyan]int kay[5]={20,30,40,50,60};\nint yoka[]={20,30,40,50,60};[/cyan]")
    
    programmecode = '''#include<stdio.h>  
    int main() {      
    int i=0; 
    int hue[5]={20,30,40,50,60}; // Declaration & Initialization of array hue with provided size
    int dogesh[]={8,4,3,6,9}; // Declaration & Initialization of array hue w/o provided size
    //traversal of array    
    for(i=0;i<5;i++){      
        printf("%d ",hue[i]);
    }    
    printf("4th element at 3rd index in array dogesh is: %d ",dogesh[3]);  // 6
    return 0;  
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nArrays in C\n", style="cyan")
                console.print(notes, style=dim_yellow)
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nArrays in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def arrays_two_dim_19():
    table = Table(title="2-D Arrays in C", show_header=True)
    table.add_column("Declaration")
    table.add_column("Initialization")
    table.add_column("Declaration & Initialization")

    table.add_row("[cyan]data_type array_name[rows_size][column_size];\nint omkey[3][4];[/cyan]",
        "[cyan]omkey[0][1]=1;\nomkey[1][2]=69;[/cyan]",
        "[cyan]int kay[3][2]={ {20,30},{40,50},{90,60} };\nint yoka[][4]={ {20,30,40,50},{60,34,85,21} };[/cyan]")
    
    programmecode = '''#include <stdio.h>
    int main() {
    // An array with 4 rows and 2 columns
    int omkey[4][2] = { {0, 0}, {1,2}, {2,4}, {3,6} };
    int i, j;

    // Output each array element's value
    for(i=0; i<4; i++){
        for(j=0; j<2; j++){
            printf("omkey[%d][%d] = %d ", i,j, omkey[i][j] );
        } 
    }
    return 0;
}

<-------------------- OR -------------------->

#include <stdio.h>
    int main() {
    // An array with 4 rows and 2 columns
    int omkey[4][2];
    int i, j;
    // Take input of the elements of array omkey
    for(i=0; i<4; i++){
        for(j=0; j<2; j++){
            scanf("%d", &omkey[i][j] );
        }
    }

    // Output each array element's value
    for(i=0; i<4; i++){
        for(j=0; j<2; j++){
            printf("omkey[%d][%d] = %d", i,j, omkey[i][j] );
        } 
    }
    return 0;
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\n2-D Arrays in C\n", style="cyan")
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\n2-D Arrays in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def arrays_search_sorting_20():
    notes = '''
 ► Searching 
    • Linear Search (For unsorted array)
	• Binary Search (For sorted array)
        • Recursive approach
        • Iterative approach

 ► Sorting 
	• Bubble Sorting
	• Selection Sorting
    • Insertion Sorting
'''
    programmecode = '''<-------------------- Searching for an element in an Array -------------------->

1. Linear Search

#include <stdio.h>

int main() {
    int arr[100];
    int size, toSearch, found, i;

    printf("Enter size of array: ");
    scanf("%d", &size);

    printf("Enter elements in array: ");
    for(i=0; i<size; i++){
        scanf("%d", &arr[i]);
    }
    
    printf("Enter element to search: ");
    scanf("%d", &toSearch);

    found = 0;

    for(i=0; i<size; i++){
        if (arr[i] == toSearch){
            found = 1;
            break;
        }
    }
    if(found == 1){
        printf("%d is found at position %d", toSearch, i + 1);
    }
    else{
        printf("%d is not found in the array", toSearch);
    }
    return 0;
}

2. Binary Search
    2.1 Iterative approach

#include <stdio.h>

int iterativeBinarySearch(int array[], int start_index, int end_index, int element){
   while (start_index <= end_index){
      int middle = start_index + (end_index- start_index )/2;
      if (array[middle] == element)
         return middle;
      if (array[middle] < element)
         start_index = middle + 1;
      else
         end_index = middle - 1;
   }
   return -1;
}

int main(void){
   int array[] = {1, 4, 7, 9, 16, 56, 70};
   int n = 7; // Array size
   int element = 16; // Element to find in Array
   int found_index = iterativeBinarySearch(array, 0, n-1, element); // Caling the function iterativeBinarySearch()
   
   if(found_index == -1 ) {
      printf("Element not found in the array. ");
   }
   else {
      printf("Element found at index: %d",found_index);
   }
   return 0;
}

<-------------------- Sorting an Array -------------------->

1. Bubble Sorting

#include<stdio.h>

int main() {
   int a[50], i,j,n,t;
   printf("Input the no. of elements in the list: ");
   scanf("%d", &n);
   
   printf("Input the elements: ");
   for(i=0; i<n; i++){
      scanf ("%d", &a[i]);
   }
   
   printf("Before Bubble Sorting the elements are: ");
   for(i=0; i<n; i++)
      printf("%d ", a[i]);
   for (i=0; i<n-1; i++){
      for (j=i+1; j<n; j++){
         if (a[i] > a[j]){
            t = a[i];
            a[i] = a[j];
            a[j] = t;
         }
      }
   }

   printf ("After Bubble Sorting the elements are: ");
   for (i=0; i<n; i++)
      printf("%d ", a[i]);
   return 0;
}

2. Selection Sorting

#include <stdio.h>

int main() {
    int a[100], n, i, j, position, swap;
    printf("Input no.s of elements: ");
    scanf("%d", &n);
    printf("Input %d Numbers: ", n);
    
    for(i=0; i<n; i++)
        scanf("%d", &a[i]);
    
    for(i=0; i<n - 1; i++){
        position = i;
        for(j=i+1; j<n; j++){
            if(a[position] > a[j])
                position = j;
        }
        if(position != i){
            swap = a[i];
            a[i] = a[position];
            a[position]=swap;
        }
    }

    printf("Sorted Array: ");
    for(i=0; i<n; i++)
        printf("%d ", a[i]);
    return 0;
}

3. Insertion Sorting

#include <stdio.h>
#include <math.h>

// Insertion Sort Function
void insertionSort(int array[], int n) {
    int i, element, j;
    for(i=1; i<n; i++){
        element = array[i];
        j = i - 1;
        while(j>=0 && array[j] > element){
            array[j + 1] = array[j];
            j = j - 1;
        }
        array[j + 1] = element;
    }
}

// Function to print the elements of an array
void printArray(int array[], int n) {
    int i;
    for (i = 0; i < n; i++)
        printf("%d ", array[i]);
}

// Main & Important Function
int main() {
    int arr[100], n;
    printf("Input no.s of elements: ");
    scanf("%d", &n);
    printf("Input %d Numbers: ", n);

    for(int i=0; i<n; i++)
        scanf("%d", &arr[i]);
    insertionSort(arr, n);
    printArray(arr, n);
    return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Programme Code\n2. Exit", style=dim_yellow)
    def t_c_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print(templatecode)
                t_c_func()
            elif i_ochoice==2:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                t_c_func()
        except:
            t_c_func()
    t_c_func()


def string_intro_21(): 
    notes= '''A string is a sequence of characters enclosed in the double quotation marks & terminated with a null character /0.
    
    ► strlen(str)  [Returns the length of a string, not counting the or NULL character at the end of the string]
    //syntax > strlen(str)

    ► strcmp(str, str1)  [Compares two strings in a case-sensitive way. If str == str1, the function returns 0]
    //syntax > strcmp(dest, src)==0
    
    ► strrev(str)  [The strrev() function is used to reverse the given string]
    //syntax > strrev(str)
    
    ► strcpy(str, str1)  [Copies str1 content to str]
    //syntax > strcmp(dest, src)
    
    ► strcat(str, str1)  [Appends str1 to str string, creating a single string out of two]
    //syntax > strcat(dest, src)
    '''

    table = Table(title="Strings in C", show_header=True)
    table.add_column("Declaration")
    table.add_column("Initialization")

    table.add_row("[cyan]data_type string_name[size];\nchar s[5];[/cyan]",
        "[cyan]char strng[] = 'abcd';\nchar strng[50] = 'abcd';\nchar strng[] = {'a', 'b', 'c', 'd', '\0'};\nchar strng[5] = {'a', 'b', 'c', 'd', '\0'};[/cyan]")


    programmecode='''#include <stdio.h>
#include <string.h>

int main() {
    int a, b;
    char strng[30];
    char strng2[30];
    char strng3[30] = "Programming in C";
    char ch = 'P';
    char strng4[30] = "in";
    char *fstrng;

    printf("Enter first string: ");
    gets(strng);

    printf("Enter second string: ");
    gets(strng2);

    while(1){
        printf("/nString Operations:/n 1. String length/n 2. String Copy/n 3. String Comparison /n 4. String Concatenation /n 5. String Reverse /n 6. Find the first occurenece of character in string /n 7. Find the substring in other string /n 8. Exit/n");
        printf("Enter the operation you wish to perform (1-8): ");
        scanf("%d", &a);

        switch(a){
        case 1:
            b = strlen(strng);
            printf("/nLength of the string is: %d./n", b);
            break;

        case 2:
            strcpy(strng, strng2);
            printf("/nCopied string is: %s./n", strng);
            break;

        case 3:
            b = strcmp(strng, strng2);
            if (b == 0)
                printf("Both strings are same./n");

            else
                printf("Both strings are different./n");
            break;

        case 4:
            strcat(strng, strng2);
            printf("/nConcatenated string is: %s./n", strng);
            break;

        case 5:
            strrev(strng);
            printf("/nReversed string is: %s./n", strng);
            break;
        
        case 6:
            fstrng = strchr(strng3, ch);
            printf("Found first occurence of character %c from: %s", ch, fstrng);
            break;
        
        case 7:
            if(strstr(strng3, strng4)){
            printf("/nSub-string Found");
            }
            else{
                printf("Not found!");
            }
            break;

        case 8:
            return 0;

        default:
            printf("You entered an invalid option./n");
        }
    }
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nStrings in C\n", style="cyan")
                console.print(notes, style=dim_yellow)
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nStrings in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def functions_intro_22():
    notes= '''► A function is a group of statements that together perform a task.
► Every C program has at least one function, which is main().
► A function declaration tells the compiler about a function's name, return type, and parameters. 
► A function definition provides the actual body of the function.
► Standard library functions
    • The standard library functions are built-in functions in C programming
    • These functions are defined in header files. #include <stdio.h> -> printf(), scanf()
    • Examples: printf(), scanf(), gets(), puts(), ceil(), floor(), etc.

► User-defined functions
    • Functions which are created by the C programmer, so that he/she can use it many times.
    • It reduces the complexity of a big program and optimizes the code.
'''

    table = Table(title="Functions in C", show_header=True)
    table.add_column("Function declaration")
    table.add_column("Function definition")
    table.add_column("Function call")

    table.add_row("[cyan]return_type function_name(argument list);[/cyan]",
        "[cyan]return_type function_name(argument list) { function body; }[/cyan]",
        "[cyan]function_name(argument_list);[/cyan]")


    programmecode='''<----- Template ----->
    
return_type function_name(data_type parameter...){  
    //code to be executed  
}

<-------------------- Function do not return any value -------------------->

#include <stdio.h>

void hello(){  
    printf("hello c");
}

<------------------------ Function do return value ------------------------>

#include <stdio.h>

//Int 
int get(){  
    return 10;  
}

// Float
float get(){  
    return 10.2;  
}  

// Character
char get(){  
    return 'a';  
}  

<-------------------- CODE -------------------->

#include<stdio.h>  

void printName();  // Function Declaration
  
void main() {
    printf("Hellew ");  
    printName(); // Function call
}

void printName() {  
    printf("World");  
}

<--------------------- OR --------------------->

#include<stdio.h>  

// Function Declaration & Definition
void printName() {  
    printf("World");  
}

void main() {
    printf("Hellew ");  
    printName(); // Function call
}

<------------------------- Function with arguments ------------------------->

#include<stdio.h>  

// Function Declaration & Definition with arguments a & b
void sum(int a, int b) {
    int k;
    k=a+b;
    printf("%d", k);  
}

void main() {
    int a, b;
    scanf("%d", &a);
    scanf("%d", &b);
    sum(a, b); // Function call
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nFunctions in C\n", style="cyan")
                console.print(notes, style=dim_yellow)
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nFunctions in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def functions_user_defined_23(): 
    programmecode = '''<-------------------- CODE -------------------->

#include<stdio.h>

int multiply(int a, int b); // Function Declaration with Arguments

int main() {
    int a, b, result;
    printf("Please input 2 numbers that you want to multiply: ");
    scanf("%d %d", &a, &b);
    result = multiply(a, b); // Function call and storing it in result var
    printf("The result of muliplication is: %d", result);
    return 0;
}

int multiply(int a, int b) {
    return (a*b); // Function Defintion
}

<-------------------- OR -------------------->

#include<stdio.h>

int multiply(int a, int b) {
    return (a*b); // Function Defintion
}

int main() {
    int a, b, result;
    printf("Please input 2 numbers that you want to multiply: ");
    scanf("%d %d", &a, &b);
    result = multiply(a, b); // Function call and storing it in result var
    printf("The result of muliplication is: %d", result);
    return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Programme Code\n2. Exit", style=dim_yellow)
    def t_c_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nUser-Defined Functions in C\n", style="cyan")
                console.print(templatecode)
                t_c_func()
            elif i_ochoice==2:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                t_c_func()
        except:
            t_c_func()
    t_c_func()


def functions_recurrsive_24():
    notes= '''► A function that calls itself is known as a recursive function.
► This technique is known as recursion.
'''
    programmecode = '''<-------------------- Template -------------------->

void recursion() {
   recursion(); // Function calls itself
}

int main() {
   recursion();
}

<-------------------- CODE -------------------->

#include <stdio.h>

int sum(int n) {
    if(n != 0) // if n is not equals to 0
        return n + sum(n-1); // sum() function calls itself 
    else
        return n;
}

int main() {
    int num, result;

    printf("Input a positive integer: ");
    scanf("%d", &num);
    result = sum(num);
    printf("Sum of %d natural numbers = %d",num ,result);
    return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nRecurrsive Functions in C\n", style="cyan")
                console.print(notes, style=dim_yellow)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nRecurrsive in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def intro_macros_25(): 
    notes= '''► A macro is a segment of code which is replaced by the value of macro. 
► Macro is defined by #define directive.
► There are two types of macros:
    • Object-like Macros
    • Function-like Macros
'''

    table = Table(title="Macros in C", show_header=True)
    table.add_column("Object-like Macros")
    table.add_column("Function-like Macros")

    table.add_row("[cyan]#define PI 3.14[/cyan]",
        "[cyan]#define MIN(a,b) ((a)<(b)?(a):(b))[/cyan]")


    programmecode='''<-------------------- CODE -------------------->
#include <stdio.h>
#define PI 3.1415  // Object-like Macros
#define circleArea(r) (PI*r*r)  // Function-like Macros

int main() {
    float radius, area;

    printf("Enter the radius: ");
    scanf("%f", &radius);
    area = circleArea(radius);
    printf("Area = %.2f", area);

    return 0;
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nMacros in C\n", style="cyan")
                console.print(notes, style=dim_yellow)
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nMacros in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def pointers_basics_26(): 
    notes= '''► The pointer in C language is a variable which stores the address of another variable. 
► This variable can be of type int, char, array, function, or any other pointer. 
► The size of the pointer depends on the architecture. 
► In 32-bit architecture the size of a pointer is 2 byte. 
► Types of Pointers:
    • Null pointer - A null pointer always contains value 0.
    • Void pointer - A Generic Pointer that has no associated data type with it, can hold addresses of any data type
      and can be typecast to any data type.
    • Wild pointer - Uninitialized Pointers point to some arbitrary memory location and may cause a program to crash
      or behave badly.
    • Dangling pointer - Pointer that actually points to a specific memory location that is to be free or deleted
      later.
'''

    table = Table(title="Pointers in C", show_header=True)
    table.add_column("Declaration")
    table.add_column("Initialization")

    table.add_row("[cyan]data_type *variable_name;\nint a = 10;\nint *ptr;[/cyan]",
        "[cyan]ptr = &a[/cyan]")


    programmecode='''<-------------------- CODE -------------------->
#include <stdio.h>

int main() {
   int  num = 20;
   int  *ptr; // Pointer Variable Declaration
   ptr = &num;  /* store address of var in pointer variable*/

   printf("Address of num variable: %p/n", &num);

   // Address stored in pointer variable ptr
   printf("Address stored in ptr variable: %p/n", ptr);

   // Access the value using the pointer
   printf("Value of *ptr variable: %d/n", *ptr);  // NOTE: Astrics (*) is important to use pointers
   return 0;
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nPointers in C\n", style="cyan")
                console.print(notes, style=dim_yellow)
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nPointers in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def pointer_pointer_airthmetic_27(): 
    table = Table(title="Pointer to Pointers in C", show_header=True)
    table.add_column("Declaration")
    table.add_column("Initialization")

    table.add_row("[cyan]data_type **variable_name;\nint a = 10;\nint *ptr\nint **ptr2;[/cyan]",
        "[cyan]ptr = &a\nptr2 = &ptr[/cyan]")


    programmecode='''<-------------------- CODE -------------------->
#include <stdio.h>
 
int main () {

   int  num; // Declaration
   int  *ptr;
   int  **ptr2;
   num = 3000; // Initialization

   // Take the address of num
   ptr = &num;

   // Take the address of ptr using address of operator &
   ptr2 = &ptr;

   // Take the value using ptr2
   printf("Value of num = %d/n", num);
   printf("Value available at *ptr = %d/n", *ptr);
   printf("Value available at **ptr2 = %d/n", **ptr2);
   return 0;
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nPointer to Pointers in C\n", style="cyan")
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nPointer to Pointers in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def pointer_array_28():
    table = Table(title="Pointer to Arrays in C", show_header=True)
    table.add_column("Declaration")
    table.add_column("Initialization")

    table.add_row("[cyan]data_type *variable_name;\nint arr[5] = {1,2,3,4,5};\nint *ptr;[/cyan]",
        "[cyan]ptr = arr\nOR\nptr = &arr[0][/cyan]")


    programmecode='''<-------------------- CODE -------------------->
#include<stdio.h>

    int main() {
    int arr[5] = { 1, 2, 3, 4, 5 };
    int *ptr = arr; // OR *ptr = &arr[0]
    printf("%p/n", ptr);
    return 0;
}
'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nPointer to Arrays in C\n", style="cyan")
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nPointer to Arrays in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def pointer_functions_29():
    table = Table(title="Pointer to Functions in C", show_header=True)
    table.add_column("Declaration")
    table.add_column("Initialization")

    table.add_row("[cyan]return type (*pointer_name)(type1, type2…);\nint add(int,int);\nint (*ptr)(int,int);[/cyan]",
        "[cyan]ptr = add;\nresult=(*ptr)(a,b);[/cyan]")


    programmecode='''<-------------------- CODE -------------------->
#include <stdio.h>  

int add(int a,int b) {  
    int c=a+b;  
    return c;  
}

int main() {  
    int a,b;  
    int (*hue)(int,int); // Declaration of a function pointer   
    int result;  
    printf("Input the values of a and b: ");  
    scanf("%d %d", &a, &b);  
    hue = add;  // Assigning address of function to the hue pointer 
    result=(*hue)(a,b);  // Calling a function using function pointer 
    printf("Value after addition is: %d",result);  
    return 0;  
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nPointer to Functions in C\n", style="cyan")
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nPointer to Functions in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def storage_classes_intro_30(): 
    notes= '''► In C language, each variable has a storage class which decides the following things: 
    • Scope - Where the value of the variable would be available inside a program.
    • Default initial value - If we do not explicitly initialize that variable, what will be its default initial value.
    • Lifetime of that variable - For how long will that variable exist.
'''

    table = Table(title="Storage Classes in C", show_header=True)
    table.add_column("Storage Classes")
    table.add_column("Storage Place")
    table.add_column("Default Value")
    table.add_column("Scope")
    table.add_column("Lifetime")

    table.add_row("[cyan]auto\n[/cyan]",
        "[cyan]RAM\n[/cyan]",
        "[cyan]Garbage Value\n[/cyan]",
        "[cyan]Local\n[/cyan]",
        "[cyan]Within function\n[/cyan]")

    table.add_row("[cyan]extern[/cyan]",
        "[cyan]RAM[/cyan]",
        "[cyan]Zero[/cyan]",
        "[cyan]Global[/cyan]",
        "[cyan]Till the end of the main program maybe declared anywhere in the program\n[/cyan]")
    
    table.add_row("[cyan]static[/cyan]",
        "[cyan]RAM[/cyan]",
        "[cyan]Zero[/cyan]",
        "[cyan]Local[/cyan]",
        "[cyan]Till the end of the main program, Retains value between multiple functions call\n[/cyan]")

    table.add_row("[cyan]register[/cyan]",
        "[cyan]Register[/cyan]",
        "[cyan]Garbage Value[/cyan]",
        "[cyan]Local[/cyan]",
        "[cyan]Within function[/cyan]")


    programmecode='''<-------------------- CODE -------------------->
#include <stdio.h>  
    int hue=9;  // Global Scope
    static float f; // Static
    
    int main() {
    int omkey; // Auto -> Default is Garbage Value
    extern int hue; // Extern
    register int a;  // Register -> Default is Garbage Value
    
    printf("%d/n",a);  
    printf("%d/n",hue);  
    printf("%f/n",f);  
    printf("%d/n",omkey);  
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nStorage Classes in C\n", style="cyan")
                console.print(notes, style=dim_yellow)
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nStorage Classes in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def structure_basics_31():
    notes= '''► Structure in c is a user-defined data type that enables us to store the collection of different data types. 
► Each element of a structure is called a member. 
► The 'struct' keyword is used to define the structure. 
► Syntax to define the structure in c:
    • struct structure_name {
        data_type member1;  
        data_type member2;  
        .    
        data_type memeberN;  
      };
'''

    table = Table(title="Structures in C", show_header=True)
    table.add_column("Declaration of structure")
    table.add_column("Declaration of variables")

    table.add_row("[cyan]struct structure_name {\ndata_type member1;\ndata_type member2;\n.\ndata_type memeberN;\n};[/cyan]",
        "[cyan]struct employee e1, e2;[/cyan]")


    programmecode='''<-------------------- CODE -------------------->
#include<stdio.h>  
#include <string.h>    

struct employee {
    int id;
    char name[50];
}e1;   // Declaring e1 variable for structure inside structure

int main() {    
    e1.id = 16969;  // Store first employee id
    strcpy(e1.name, "4n5hu");  // Copying name of second employee string into char array
    printf("Employee e1 id: %d/n", e1.id);  // Printing first employee id        
    printf("Employee e1 name: %s/n", e1.name);   // Printing first employee name
    return 0;
}  

<-------------------- OR -------------------->

#include<stdio.h>  
#include <string.h>    

struct employee {
    int id;
    char name[50];
};    

int main() {
    struct employee e1, e2;  // Declaring e1 variable for structure  
    e1.id = 16969;  // Store first employee id
    strcpy(e1.name, "4n5hu");  // Copying name of first employee string into char array
    e2.id = 5902;  // Store second employee id
    strcpy(e2.name, "Cheems");  // Copying name of second employee string into char array

    printf("Employee e1 id: %d/n", e1.id);  // Printing first employee id        
    printf("Employee e1 name: %s/n", e1.name);   // Printing first employee name
    printf("Employee e2 id: %d/n", e2.id);  // Printing second employee id        
    printf("Employee e2 name: %s/n", e2.name);   // Printing second employee name
    return 0;
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nStructures in C\n", style="cyan")
                console.print(notes, style=dim_yellow)
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nStructures in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def structure_nested_array_32(): 
    table = Table(title="Types Of Nested Struture in C", show_header=True)
    table.add_column("By Separate Structure")
    table.add_column("By Embedded Structure")

    programmecode='''<-------------------- By Separate Structure -------------------->
#include<stdio.h>

struct info {  
    int date;  
    char month[20];  
    int year;  
};

struct employee {  
    char name[20];
    char city[50];
    struct info add;  
};

void main() {  
    struct employee emp;  
    printf("<----- Enter employee Details----->/n");
    printf("Input employee Name: ");
    gets(emp.name);
    printf("Input employee City: ");
    scanf("%s", emp.city);
    printf("Input employee Date(02) of joining: ");
    scanf("%d", &emp.add.date);
    printf("Input employee Month(Jan) of joining: ");
    scanf("%s", emp.add.month);
    printf("Input employee year(2010) of joining: ");
    scanf("%d", &emp.add.year);
    printf("/n<----- Stored Employee Information ----->/n");  
    printf("Name: %s/nCity: %s/nDate Of Joining: %d %s %d", emp.name, emp.city, emp.add.date, emp.add.month, emp.add.year);  
}

<-------------------- By Embedded Structure -------------------->

#include <stdio.h>  
#include <string.h>  

struct Employee {     
   int id;
   char name[20];

   struct Date {  
      int date;  
      int mon;
      int yr;   
    }doj;
}e1;

int main() {  
   e1.id=101;  
   strcpy(e1.name, "Cheems Pandey"); // Copying string into char array name  
   e1.doj.date=20;  
   e1.doj.mon=05;  
   e1.doj.yr=2021;  
  
   printf("Employee id: %d/n", e1.id);  
   printf("Employee name: %s/n", e1.name);  
   printf("Employee date of joining (dd/mm/yyyy): %d/%d/%d", e1.doj.date, e1.doj.mon, e1.doj.yr);  
   return 0;  
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nNested Struture in C\n", style="cyan")
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nNested Struture with arrays in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def structure_funct_33():
    table = Table(title="Types of Methods to play with Struture & Functions in C", show_header=True)
    table.add_column("Passing structure to a function by value")
    table.add_column("Passing structure to a function by address(reference)")
    table.add_column("No need to pass a structure – Declare structure variable as global")

    programmecode='''<-------------------- Passing structure to a function by value -------------------->
#include <stdio.h>

struct student {
   char name[50];
   int age;
};

// Function Prototype
void display(struct student stu);

int main() {
   struct student s1;

   printf("Input Student name: ");
   // Read string input from the user until '/n' is entered
   // '/n' is discarded
   scanf("%[^/n]%*c", s1.name);

   printf("Input age: ");
   scanf("%d", &s1.age);

   display(s1); // Passing struct s1 as an argument in display() function
   return 0;
}

void display(struct student s) {
   printf("/n<----- Displaying information ----->/n");
   printf("Name: %s/n", s.name);
   printf("Age: %d", s.age);
}

<-------------------- Passing structure to a function by address(reference) -------------------->

#include <stdio.h>

struct student {
   char name[50];
   int age;
};

// Function Prototype with Pointer
void display(struct student *stu);

int main() {
   struct student s1;

   printf("Input Student name: ");
   // Read string input from the user until /n is entered
   // /n is discarded
   scanf("%[^/n]%*c", s1.name);

   printf("Input age: ");
   scanf("%d", &s1.age);

   display(&s1); // Passing address of struct s1 as an argument in display() function
   return 0;
}

void display(struct student *s) {
   printf("/n<----- Displaying information ----->/n");
   printf("Name: %s/n", s->name);
   printf("Age: %d", s->age);
}

<-------------------- No need to pass a structure – Declare structure variable as global -------------------->

#include <stdio.h>

struct student {
   char name[50];
   int age;
};

struct student stu1;  // Global declaration of Structure stu1

// Function Prototype
void display();

int main() {
   printf("Input Student name: ");
   // Read string input from the user until \n is entered
   // \n is discarded
   scanf("%[^\n]%*c", stu1.name);

   printf("Input age: ");
   scanf("%d", &stu1.age);

   display();  // Calling the display function
   return 0;
}

void display() {
   printf("\n<----- Displaying information ----->\n");
   printf("Name: %s\n", stu1.name);
   printf("Age: %d", stu1.age);
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nStruture & Functions in C\n", style="cyan")
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nStruture & Functions in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def DMA_basics_34(): 
    notes= '''► The concept of Dynamic Memory Allocation (DMA) in C language enables the C programmer to allocate memory at runtime. 
► Dynamic memory allocation in C language is possible by 4 functions of stdlib.h header file. 
'''

    table = Table(title="DMA in C", show_header=True)
    table.add_column("malloc()")
    table.add_column("calloc()")
    table.add_column("realloc()")
    table.add_column("free()")

    table.add_row("[cyan]Allocates single block of requested memory\npointer = (cast-type*)malloc(byte-size)[/cyan]",
        "[cyan]Allocates multiple block of requested memory\npointer = (cast-type*)calloc(number, byte-size)[/cyan]",
        "[cyan]Reallocates the memory occupied by malloc() or calloc() functions\npointer = realloc(pointer, new-size)[/cyan]",
        "[cyan]Frees the dynamically allocated memory\nfree(pointer)[/cyan]")

    programmecode='''<-------------------- CODE -------------------->

<---------------- Malloc & Free---------------->

// Program to calculate the sum of n numbers inputted by the user

#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i, *pointer, sum = 0;
    printf("Input the number of elements: ");
    scanf("%d", &n);
    pointer = (int*) malloc(n * sizeof(int));  // Allocating memory to pointer according to the data type provided 

    // If memory cannot be allocated
    if(pointer == NULL) {
      printf("Error! memory not allocated.");
      exit(0);
    }
    printf("Input elements: ");
    for(i = 0; i < n; ++i) {
      scanf("%d", pointer + i);
      sum += *(pointer + i);
    }
    printf("Sum = %d", sum);

    // Deallocating/Freeing-up the memory
    free(pointer);
    return 0;
}

<---------------- Calloc & Free ---------------->

// Program to calculate the sum of n numbers inputted by the user

#include <stdio.h>
#include <stdlib.h>

int main() {
    int n, i, *pointer, sum = 0;
    printf("Input the number of elements: ");
    scanf("%d", &n);
    pointer = (int*) calloc(n, sizeof(int));  // Allocating memory to pointer according to the data type provided 

    // If memory cannot be allocated
    if(pointer == NULL) {
      printf("Error! memory not allocated.");
      exit(0);
    }
    printf("Input elements: ");
    for(i = 0; i < n; ++i) {
      scanf("%d", pointer + i);
      sum += *(pointer + i);
    }
    printf("Sum = %d", sum);

    // Deallocating/Freeing-up the memory
    free(pointer);
    return 0;
}'''
    
    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Notes\n2. Programme Code\n3. Exit", style=dim_yellow)
    def i_o_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nDMA in C\n", style="cyan")
                console.print(notes, style=dim_yellow)
                console.print(table)
                i_o_func()
            elif i_ochoice==2:
                console.print("\nDMA in C\n", style="cyan")
                console.print(templatecode)
                i_o_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                i_o_func()
        except:
            i_o_func()
    i_o_func()


def DMA_array_structure_35():
    programmecode = '''<-------------------- First Method -------------------->
#include <stdio.h>
#include <stdlib.h>

struct course {
  int marks;
  char subject[30];
};

int main() {
  struct course *crseptr;
  int rec;
  printf("Input the number of records: ");
  scanf("%d", &rec);

  // Memory allocation for rec structures
  crseptr = (struct course *)malloc(rec * sizeof(struct course));
  
  for(int i=0; i<rec; ++i) {
    printf("Enter subject and it's marks: ");
    scanf("%s %d", (crseptr + i)->subject, &(crseptr + i)->marks);
  }

  printf("<----- Displaying Information ----->\n");
  for(int i=0; i<rec; ++i) {
    printf("Subject: %s/nMarks: %d/n", (crseptr + i)->subject, (crseptr + i)->marks);
  }

  free(crseptr);

  return 0;
}

<-------------------- Second Method -------------------->

#include <stdio.h>
#include <string.h>
#include <stdlib.h>

int main() {
    int nostu;
    printf("No. of students you want to store details of: ");
    scanf("%d", &nostu);
    struct student{
        char name[50];
        int age, id;
        char grade[3];
    } lst[nostu];

    // Allocation memory
    struct student *crseptr = (struct student *)malloc(sizeof(struct student) * nostu);

    for(int i=0; i<nostu; i++){
        printf("Input the student Name: ");
        fflush(stdin);
        gets(lst[i].name);
        printf("Input the student age: ");
        scanf("%d", &lst[i].age);
        printf("Input the student id: ");
        scanf("%d", &lst[i].id);
        printf("Input the grade: ");
        scanf("%s", lst[i].grade);
        crseptr++;
    }

    for(int n=0; n<nostu; n++){
        printf("%s is %d years old, his id is %d & grade is %s./n",
               lst[n].name, lst[n].age, lst[n].id, lst[n].grade);
    }
    return 0;
}'''

    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Programme Code\n2. Exit", style=dim_yellow)
    def t_c_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nDMA with Arrays & Structures in C\n", style="cyan")
                console.print(templatecode)
                t_c_func()
            elif i_ochoice==2:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                t_c_func()
        except:
            t_c_func()
    t_c_func()


def NBWB_69():

    
    def dnwlnbwb():
        print("Downloading Programme File From Database...\n")
        try:
            cwdh=os.getcwd()
            url = "https://drive.google.com/uc?id=1OP55-MfNoo0ve7bfkS1cRwwEN6iyXdwl"
            wget.download(url, f"{cwdh}\Miscellaneous_Programme.txt")
        except Exception as e:
            print(f"Error: {e}")
        s(1)


    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Download Programme File\n2. Open Miscellaneous Programme Codes\n3. Exit", style=dim_yellow)
    def t_c_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                dnwlnbwb()
                console.print("Done! Check the downloaded file 'Miscellaneous_Programme.txt'\n")
                t_c_func()
            elif i_ochoice==2:
                if os.path.isfile("Miscellaneous_Programme.txt"):
                    heavyComtent = open("Miscellaneous_Programme.txt", "r")
                    ah=heavyComtent.read()
                    programmecode = f'''{ah}'''
                    templatecode = Syntax(programmecode, "C", theme=console_theme, line_numbers=True)
                    console.print("\nMiscellaneous Programs in C\n", style="cyan")
                    console.print(templatecode)
                    heavyComtent.close()
                    t_c_func()
                else:
                    print("File Do Not Exist!")
                    t_c_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            
            else:
                t_c_func()
        except:
            t_c_func()
    t_c_func()


def cheatsheet_99():


    def getpdfiles():
        try:
            cwdh=os.getcwd()
            url = "https://drive.google.com/uc?id=1FqvaDFgq86bMg61kt2ek4cMmZ7BzvEyY"
            wget.download(url, f"{cwdh}\FOCP_Worksheets_PDF.zip")
        except Exception as e:
            print(f"Error: {e}")


    def getdocxfiles():
        try:
            cwdh=os.getcwd()
            url = "https://drive.google.com/uc?id=14D7sDu2WZR0V6zmfzYaS7ftslxLAvGBd"
            wget.download(url, f"{cwdh}\FOCP_Worksheets_DOCX.zip")
        except Exception as e:
            print(f"Error: {e}")


    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Download Worksheets DOCXs\n2. Download Worksheets PDFs\n3. Exit", style=dim_yellow)
    def t_c_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                console.print("\nDownloading Worksheets (DOCXs) of FOCP...\n")
                getdocxfiles()
                console.print("\nDone! Check folder 'FOCP_Worksheets_DOCX.zip' & Unzip it to access the content.")
                t_c_func()
            elif i_ochoice==2:
                console.print("\nDownloading Worksheets (PDFs) of FOCP...\n")
                getpdfiles()
                console.print("\nDone! Check folder 'FOCP_Worksheets_PDF.zip' & Unzip it to access the content.")
                t_c_func()
            elif i_ochoice==3:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                t_c_func()
        except:
            t_c_func()
    t_c_func()


def aboutme():
    print(colo("\n--------------------------------------------", "magenta"))
    console.print("1. Github\n2. Linkedin\n3. Instagram\n4. Exit", style=dim_yellow)
    def t_c_func():
        try:
            i_ochoice = int(input("\nPlease select an option > "))
            if i_ochoice==1:
                wb.open_new("https://github.com/anshu189")
                t_c_func()
            elif i_ochoice==2:
                wb.open_new("https://www.linkedin.com/in/4n5hu")
                t_c_func()
            elif i_ochoice==3:
                wb.open_new("https://www.instagram.com/anshu_ck")
                t_c_func()
            elif i_ochoice==4:
                print(colo("--------------------------------------------\n", "magenta"))
                choice_by_user()
            else:
                t_c_func()
        except:
            t_c_func()
    t_c_func()


def Exit_00():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print(colo("------------------------------------------------------------------------------------------------------------------------", "blue"))
    Closing_Art=text2art("                        See   ya   Mate !")
    Closing_Art2=text2art("            Happy  Comding  ; )")
    print(colo(Closing_Art, "cyan"))
    print(colo(Closing_Art2, "cyan"))
    print(colo("------------------------------------------------------------------------------------------------------------------------", "blue"))
    print("\n\n\n\n\n\n")
    print("Exiting in", end="")
    for huehue in range(3,0,-1):
        print(".", end="")
        s(0.39)
        print(".", end="")
        s(0.39)
        print(f"{huehue}", end="")
        s(0.39)
    os._exit(0)


# functions stored in dictionary with choices as key
CHOICES = {
    1:C_intro_1,
    2:C_install_2,
    3:C_use_compile_3,
    4:algorithm_flowchart_4,
    5:C_structure_5,
    6:startr_temp_6,
    7:i_o_func_7,
    8:format_specifier_8,
    9:data_types_9,
    10:operators_10,
    11:type_casting_11,
    12:decision_statement_12,
    13:switch_13,
    14:conditional_14,
    15:looping_15,
    16:loop_nested_16,
    17:jump_statement_17,
    18:arrays_declare_initialize_18,
    19:arrays_two_dim_19,
    20:arrays_search_sorting_20,
    21:string_intro_21,
    22:functions_intro_22,
    23:functions_user_defined_23,
    24:functions_recurrsive_24,
    25:intro_macros_25,
    26:pointers_basics_26,
    27:pointer_pointer_airthmetic_27,
    28:pointer_array_28,
    29:pointer_functions_29,
    30:storage_classes_intro_30,
    31:structure_basics_31,
    32:structure_nested_array_32,
    33:structure_funct_33,
    34:DMA_basics_34,
    35:DMA_array_structure_35,
    69:NBWB_69,
    99:cheatsheet_99,
    0:Exit_00,
    77:aboutme,
    911:contentmenu
}
# in case of invalid or unavailable choice
default = lambda: print("Invalid Input! Try Again.\n")

def choice_by_user():
    try:
        choice = int(input("Choose any by entering the correct serial no. (911 for menu)> "))
    except ValueError:
        default()
        return
    # lookup the choice in the dictionary and call it
	# done in two lines for clarity :)
    function = CHOICES.get(choice, default)
	function()


if __name__ == "__main__":
    welcome()
    while True:
        choice_by_user()
