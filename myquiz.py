title welcome to trivializia 
:menu 
cls 
echo welcome to the life and death quiz
echo hope you injoy it 
echo 1) play game 
echo 2) instructions 
echo 3) exit 
if %type% == 1 goto question1 
if %type% == 2 goto instructions 
if %tupe% == 3 goto exit 
goto menu 

:instructions 
cls 
echo =-=-=-=-=-=-=-=-=-= 
echo instruction manial 
echo =-=-=-=-=-=-=-=-=-= 
echo to continue this ultimite quiz game 
echo type what we have asked you to 
echo  type. every time when you awanser a 
echo right question the text color 
echo the text color will become red. 
echo ENJOY THE QUIZ GAME! 
echo 1) play game 
echo 2) go back to menu 
set /p type= 
if %type% == 1 goto question1 
if %type% == 2 goto menu 
goto instructions 

:question1
cls
echo what is harry potter's middle name?
echo 1) Holden
echo 2) James
echo 3) Lily
echo 4) Granger
if %type% == 1 goto wrong1
if %type% == 2 goto correct1
if %type% == 3 goto wrong1
if %type% == 4 goto wrong1
goto question1

:correct1
color a
cls
echo that is correct! Nice work
echo do you want to continue?
echo 1) continue to question 2
echo 2) go back to menu
set /p type=
if %type% == 1 goto question2
if %type% == 2 goto menu
goto correct1

:wrong1
color c
echo That is wrong!!
echo The dalek will get you!
echo do you want to try again?
echo 1) try again
echo 2) go back to menu
set /p type=
if %type% == 1 goto question1
if %type% == 2 goto menu
