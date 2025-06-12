import re, sys

input_text = open( sys.argv[1], encoding="utf-8" )
text1 = input_text.read()
input_text.close()

# Criacao tokens
tokens = re.split( r'(\s|[;{}(),:"\'])', text1 )

# Criacao do vocabulario

all_words = sorted( set(tokens) )
# Special context tokens
all_words.extend( ["<|eof|>", "<|unk|>"] )

voc = { token_id:word for token_id,word in enumerate(all_words) }

class TokenizerV2:
    def __init__( self, vocab ):
        self.int_str = vocab
        self.str_int = {i:j for j,i in vocab.items()}

    def encode( self, text ):
        tokens = re.split( r'(\s|[;{}()],:"\')', text )
        tokens = [i for i in tokens if i.strip()]
        tokens = [i if(i in self.str_int) else "<|unk|>"
                  for i in tokens]

        id_list = [self.str_int[st] for st in tokens]

        return id_list

    def decode( self, numbers ):
        text = [self.int_str[i] for i in numbers]
        text = " ".join( text )
        text = re.sub( r'\s+(\s|[;{}(),:"\'])', r'\1', text )

        return text

tok2 = TokenizerV2(voc)

print( "****************" )
print( "Vocabulary length:", len(voc) )
print()
for i in voc.items(): print( i )
print( "****************" )
