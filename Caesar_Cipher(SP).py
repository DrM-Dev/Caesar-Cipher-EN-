#Caesar Cipher SP-ver  by  Dr.M-Dev:
#================================Imports
from turtle import Turtle,Screen
import time

screen = Screen()
screen.setup(500,500)
screen.bgcolor("black")
screen.title("Caesar Cipher.EN     Dr.M-Dev")

#================================


alphabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'ñ',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]


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


print("******** WELCOME TO Caesar Cipher-SP ver  -   By: Dr.m DEV *********")
print(" <!> IMPORTANT NOTE <!>\n this cipher is for Spanish-Language\n>>>>>>I have an English cipher on my github @DrM-Dev")
#==========================================================================================================
#______________________________________________________________
symbols_n_numbers = [" ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "1", "2", "3", "4", "5", "6", "7", "8", "9",]
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
        input_message = False
        decided_shift = False
        #------------
        direction = screen.textinput(title="ENCODE or DECODE",prompt="Type 'encode' to encrypt, type 'decode' to decrypt:").lower()
        text = screen.textinput(title="Input Message",prompt="Type your message:\nyou can write anything in Arabic[AR] and symbols as well").lower()
        shift = int(screen.textinput(title="Key/Shift Number",prompt="Type the shift number:"))
        #
        if direction == 'encode' or direction == 'decode':
            picked_direction = True
        if text != "":
            input_message = True
        if shift != 0:
            decided_shift = True

        #------------
        if picked_direction and input_message and decided_shift:
            still_encod_decode = False
        else:
            screen.textinput(title="⚠️Input Error", prompt="please..\n1-pick a direction to [encode or decode]\n2-write a message\n3-give a shift number more than 0\npress [OK] to try again").lower()

    #_____________________________________________________
    def decrypt(original_text = text, shift_amount = shift):
        decrypted_text = ""
        for encrypted_letters in original_text:
            if encrypted_letters in symbols_n_numbers:
                decrypted_text += encrypted_letters
            else:
                shifted_position = alphabet.index(encrypted_letters) - shift_amount
                shifted_position %= len(alphabet)
                # -------------------------------
                decrypted_text += alphabet[shifted_position]
        print(f"here's the decoded result:{decrypted_text}")
        #
        time.sleep(1)
        #
        text_draw.goto(0, 0)
        text_draw.write(f"here's the decoded result:\n\n{decrypted_text}\n\nℹ️ check terminal to copy it :)", align="Center",
                          font=("Arial", 15, "bold"))

#________________________________________________________________________________________
    def encrypt( original_text = text, shift_amount = shift):
        encrypted_text = ""
        for letter in original_text:
            if letter in symbols_n_numbers:
                encrypted_text += letter
            else:
                shifted_position = alphabet.index(letter) + shift_amount
                shifted_position %= len(alphabet) #THIS IS VITAL!!!!!! CHECK LAST NOTE BELOW [(<+>)]
                # -------------------------------
                encrypted_text += alphabet[shifted_position]
        print(encrypted_text)
        #
        time.sleep(1)
        #
        text_draw.goto(0, 0)
        text_draw.write(f"here's the encrypted result:\n\n{encrypted_text}\n\nℹ️ check terminal to copy it :)", align="Center",
                          font=("Arial", 15, "bold"))

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
                                 prompt="Do you wanna run the code to encode/decode a message?\n[yes]/[no]?").lower()

    if off_or_on == "yes":
        caesar()
        off_or_on = ""
    elif off_or_on == "no":
        print("exciting code :)")
        text_draw.write("Exciting code :)",
                        align="Center",
                        font=("Arial", 20, "bold"))
        exit_code = True
        screen.bye()

#===================================
screen.mainloop()
