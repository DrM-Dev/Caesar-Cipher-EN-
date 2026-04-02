#Caesar-Cipher / English-ver    -    By:  Dr.M-Dev
#================================Imports
from turtle import Turtle,Screen
import time
from tkinter import filedialog

screen = Screen()
screen.setup(500,500)
screen.bgcolor("black")
screen.bgpic("BG.png")
screen.title("Caesar Cipher.EN")

#================================
def logo():
    print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')

logo()
print("**** WELCOME to Caesar-Cipher [EN]-ver    -by-    Dr.M-Dev ****")
#______________________________________________________________
#______________________________________________________________
#______________________________________________________________
#______________________________________________________________
#______________________________________________________________
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
#update (adding capitalized letters):
alphabet2 = [letter.capitalize() for letter in alphabet]
alphabet.extend(alphabet2)
#______________________________________________________________
symbols_n_numbers = [" ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "?", ">", "<", ":", '"', "'", "[" , "]", "{", "}", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "`", "~", ",", ".", 1, 2, 3, 4, 5, 6, 7, 8, 9, 0,"\n"]
#________________
exit_code = False
#________________
text_draw = Turtle()
text_draw.penup()
text_draw.hideturtle()
text_draw.color("white")

#=================================================================================================
def caesar():
    #defaults:
    text_draw.clear()
    #
    direction = ""
    text = ""
    shift = 0
    still_encod_decode = True
    #----------------
    while still_encod_decode:
        picked_direction = False
        #----
        picked_text_or_file = False
        input_message = False
        #----
        decided_shift = False
        #------------
        direction = screen.textinput(title="ENCODE or DECODE",prompt="Type 'ENCODE' to encrypt [make a secret message],\nType 'DECODE' to decrypt[open a secret message]").lower()
        #====================================
        text_data_type = screen.textinput(title="Text-file or Raw text",prompt="Do you want to enter:\n[1]text-file \nor \n[2]raw-text\n\nanswer with 1 or 2").lower()
        #====================================
        if text_data_type == "1":
            txt_file_path = filedialog.askopenfilename()
            with open(txt_file_path) as targeted_txt:
                imported_text = targeted_txt.read()
                #
                text = imported_text
                # debug:
                # print(text)

        if text_data_type == "2":
            text = screen.textinput(title="Input Message",
                                    prompt="Type your message:\nyou can write anything in English[EN] and symbols as well").lower()

        #====================================
        try:
            shift = int(screen.textinput(title="Key/Shift Number",prompt="Type the shift number:"))
        except ValueError:
            text = screen.textinput(title="🛑Shift-Key is EMPTY🛑",
                                    prompt="you can't have an empty shift key or 0 shift number :(").lower()

        #
        #
        #
        #
        if direction == 'encode' or direction == 'decode':
            picked_direction = True
        #_____________
        if text_data_type == "1" or text_data_type == "2":
            picked_text_or_file = True
        #_____________
        if text != "":
            input_message = True

        if shift != 0:
            decided_shift = True
        #_____________
        if picked_direction and picked_text_or_file and input_message and decided_shift:
            still_encod_decode = False
        else:
            still_encod_decode = True
            screen.textinput(title="🛑Input Error🛑", prompt="please..\n1-pick a direction to [encode or decode]\n2-open a [1]text-file or [2]write text\n3-give a shift number more than 0\n\nPress [OK] to try again").lower()


    #_____________________________________________________
    def decrypt(original_text = text, shift_amount = shift):
        decrypted_text = ""
        for encrypted_letters in original_text:
            if encrypted_letters in symbols_n_numbers:
                # old system:
                decrypted_text += encrypted_letters
                ## -------------------------------
            else:
                # list extension trick (infinit loop)
                ## -------------------------------
                shifted_position = alphabet.index(encrypted_letters) - shift_amount
                shifted_position %= len(alphabet)
                decrypted_text += alphabet[shifted_position]

    #############PRINTING RESULTS:
        print(decrypted_text)
        with open("Decrypted Text.txt", mode="w") as file:
            file.write(decrypted_text)
        #
        # time.sleep(1)
        #
        text_draw.goto(0, 0)
        text_draw.write(
            f"ℹ️\nYour encrypted result is in terminal :)\nor\ngo to the program directory and get the text file as\n\n(Decrypted Text.txt)",
            align="Center",
            font=("Arial", 8, "bold"))
        #
        print("ℹ️\nALL DONE!\nthe program will be restarting, to encode/decode again...")
        time.sleep(4)


#________________________________________________________________________________________
    def encrypt( original_text = text, shift_amount = shift):
        encrypted_text = ""
        for letter in original_text:
            if letter in symbols_n_numbers:
                #old system:
                encrypted_text += letter
                ## -------------------------------
            else:
                try:
                    shifted_position = alphabet.index(letter) + shift_amount
                    shifted_position %= len(alphabet)
                    # -------------------------------
                    encrypted_text += alphabet[shifted_position]
                except ValueError:
                    print("⚠️\na character was outside of the encryption-limit\n some characters may remain the same")
                    print(f"⚠️THE CHARACTER >>>>>>>>>>>>>>>>>>> {letter}")

    #############PRINTING RESULTS:
        print(encrypted_text)
        with open("Encrypted Text.txt",mode="w") as file:
            file.write(encrypted_text)
        #
        # time.sleep(1)
        #
        text_draw.goto(0, 0)
        text_draw.write(f"ℹ️\nYour encrypted result is in terminal :)\nor\ngo to the program directory and get the text file as\n\n(Encrypted Text.txt)", align="Center",
                          font=("Arial", 8, "bold"))
        #
        print("ℹ️\nALL DONE!\nthe program will be restarting, to encode/decode again...")
        time.sleep(4)

#________________________________________________________________________________________
    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
        direction = ""
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
        direction = ""


#==================================USAGE:
while not exit_code:
    off_or_on = screen.textinput(title="Welcome :)",
                                 prompt="Do you wanna run the code to encode/decode a message?\nPress [OK]/Enter to proceed\nType \"END\" to exit the program").lower()

    if off_or_on == "":
        caesar()
        off_or_on = ""
    elif off_or_on == "end":
        print("exciting code :)")
        text_draw.write("Exciting code :)",
                        align="Center",
                        font=("Arial", 20, "bold"))
        exit_code = True
        screen.bye()

#===================================
screen.mainloop()
