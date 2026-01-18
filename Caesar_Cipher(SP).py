#Caesar Cipher SP-ver  by  Dr.M-Dev:

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
print(" <!> IMPORTANT NOTE <!>\n this cipher is for Arabic-Language\n>>>>>>I have an English cipher on my github @DrM-Dev")
#==========================================================================================================
#______________________________________________________________
symbols_n_numbers = [" ", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "-", "+", "=", "1", "2", "3", "4", "5", "6", "7", "8", "9",]

exit_code = False

#=================================================================================================
def caesar():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

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

#________________________________________________________________________________________
    if direction == "encode":
        encrypt(original_text=text, shift_amount=shift)
        direction = ""
    elif direction == "decode":
        decrypt(original_text=text, shift_amount=shift)
        direction = ""


#==================================USAGE:
while exit_code == False:
    off_or_on = input("do you wanna run the code to encode/decode a message?\n[yes]/[no]?").lower()

    if off_or_on == "yes":
        caesar()
        off_or_on = ""
    elif off_or_on == "no":
        print("exciting code :)")
        exit_code = True
