
#! in Generative AI, user have to make decision that he or she has to use pretrain model or need to retrain the model for 

#! generative ai is a subset of traditional machine learning

#! large language model have been trained over billion and trillions of words with large amount of compute power.

#! more parameters contained model means you can perform more sophesticated task 

#! multiple-modality : multi-purpose model

#! llm are able to take human instructions and perform task. Text you pass or question you pass known as prompt
#! space or memory available to prompt is called as context window size of this changes from model to model
#! output of model is called completion. act of text generation using the model is called inference. completion 
#! comprise of text contained in original prompt followed by generated text. 


#* Use case of LLM:
#! NER : get all of people, organizations, companies name in output,
#! chatbot, 
#! machine translation 
#! text to image
#! Augmenting LLM : by connecting to external data sources. ex. wikipedia

#* RNN(Recurrent Neutral Network):
#! RNN :  just one word information of previous time stamp is not helpful for prediction next word for current time stamp 
#! to make good prediction model should have understanding of previous words of sentence and language is complex 
#! word can have multiple meaning ex. river bank and money bank or sentence example. teacher taught the student with book.
#! here teacher teach using book or student have book and teacher have book ?.

#*power of transformer:
#! note: power of transformer lies in ability to learn the relevance and context of all the word in sentence not just each word next to its neighbor
#! but with all other words in sentence and apply attention weights to their relationships so model learn the relavance of each word to the other words.

#* self attension layer or multi head attensions:
#! self attension layer or multi head attensions: where model analyze the relation between the token vector with the sequence of words vectors to capture the 
#! contextual dependency to reflect the importance of each word with the other in sentence.

#* explain transformer architecture : used to perform sequence to sequence task , why widely used because of the faster training and parallel processing 
#&  ex. machine translation example(english to hindi)
#&  --> In this, input from english sentence : first tokenization happen , pass this token to encoder layer where 
#&  each token is converted in to the vector representation , which is n dimensional representation used to find out 
#&  the relationship between words, then this embedding layer pass to the multi-head attension layer(self-attention to compute representations of input sequences. The multi-head self-attention mechanism allows the model to focus on different parts of the input sequence) 
#&  where we found the relevance of each word with the otherwords and get the contextual encoding. this input from 
#&  multi-head attension pass to the neural network used tyo learn complex patten then this input from network pass 
#&  to the cross multi-head attension layer
#&  --> here in decoder to predict the next word of hindi, input <start> is given to the encoder then same thing encoding happen -->
#&  positional encoding happen --> mask multihead attension (current input word can have information about previous word but,
#&                                                           previous word do not have information about current word)
#&  --> then pass to the cross-multihead attension where input from encoder and output from mask-multi head attension 
#&  comes here this process helps to find the relationship of input from encoder and output from decoder mask head attension layer 
#&  and helps to predict word when this input pass to the neural network then linear layer and then pass to softmax layer.
#&  and continue the loop by passing this output as input of decoder to predict new word.
#& The Transformer model also uses residual connections and layer normalization to facilitate training and prevent overfitting.
#! output of llm is probability distribution across the tokens. so we can compare the distribution of completion and that of training labels.
#!and use standard cross entropy function to calculate the loss between two token distribution and use that loss to update the weights in back propagation

#* summary of the transformers:
#! complete transformer architecture consist of encoder and decoder component, encoder encode input sequences
#! into deep reprtesentation of structure and meaning of input, decoder working from input token triggers uses then encoder 
#! contextual understanding to generate new tokens and it does this in loop untill stop condition reach.

#* Encoder Only model:
#! encoder only models also works for sequence to sequence but without further modification
#! input and output sequence are the same length but by adding the additional layers on this architecture you can perform 
#! training of these model, these model have bidirectional contextual information about senetnce, training happen by masking the word in sentence and objective is to predict the word called denoising 
#! classification task such as sentiment analysis, spam email classification, word classification 
#! BERT is encoder only model, ROBERTA

#* Encoder and Decoder model:
#! used to perform sequence to sequence task such as translation where input sequence and output sequence can be different
#! we can also scale the model and perform text generation task.
#! example: BART and T5 
#! used for Translation, Summarization and Question Answering

#* decoder Only model or autoregressive model:
#! training objective is to predict the next token based on previous sequence of token, predicting the next token some times called full language modeling
#! model doesn't have information about end of sentence, and make prediction of new word based on previous information thats why called the unidirectional 
#! most commonly used model as they have scaled, their capabilities have grown. these model can now generalize the most task
#! example: GPT(GEnerative Pretrained Transformer), BLOOM, LLaMA.
#! used for Text Generation.

#* Prompt Engineering:
#! we can interact with the model by creating prompt using written words not code called prompt engineering.
#! model doesn't produce the outcome in first trial you may have to revise the language in your prompt or the way that it writtens the
#! several time to get the model to behave that you want. this work to develop and improve the prompt is known as prompt engineering.
#! It is a big topic but one powerful technique to get model to produce better outcome to include the examples of task that 
#! you want the model to carry out inside the prompt. provide examples in context windows is called in-context learning
#! zero shot inference , one shot inference, few shot learning ex. movie review positive or negative , this method helps model that what actually need.encourage model to learn by example.
#! this method really helpful for smaller model.

#! Transformer's neural network architecture that replaces traditional recurrent neural networks (RNNs) and convolutional neural networks (CNNs)
#! with an entirely attention-based mechanism. 

#* 
#! some of the methods and associated configuration parameters that you can use to influence the way that the model makes the final decision about next-word generation
#! max token : token in output , top K :  select word from top k words, top-p: select the word from total probability ex p = 0.30 select that words whose probability sum = 0.30 and than chose bes if use greedy method, else select rfandom if use random sample 
#! temperature : this helps to make model creative as temperature is high(high randomness), tempertature is low then model is less creative(low randomness). or we can say that to control model to produce randomness in output
#! when value of temperature <1 model will take high probability word to give output (strongly peaked probability distribution) and >1 then probability for words from softmax layer evenly spread so randomness comes in output (broader, flatter probability distribution). this lead the model to generate high degree of randomness in output or variability in output

#* GPU RAM needed to store 1b params 
#! 1 param = 4 byte (32-bit float)
#! 1b param = 4 * 10^9  = 4GB for full precision 32 precision this are only weights 
#! also there are optimizers, gredients, activation which takes 20 bites so for training model 
#! required required 6 times the gpu ram take up by weights = 4 * 6 = 24 GB

#* To reduce the memory what there are the techniques 
#! 1) Quantization : goal is reduce the memory required to store weights of model by reducing the precision of the model weights from 32 bit floating point numbers to 16 bit floating point numbers
#! or 8 bit- integer numbers. Quantization projects the 32 bit floating point numbers into lower precision space using scaling factor calculated based on 32 bit floats. 
#! ex. if use 16 bit-floating point number memory reduce to half 24 GB to 12 GB. By Quantization we can reduce memory consuption to store the model weights
#! bfloat16(brain floating point) is hybrid of 32 bit-floating and 16 bit floating,Flant T5 have been trained on BFloat16 it stores memory 16 bit 
#! it uses 8 bit to reprtesent the exponent but reduce the truncate fraction to 7 bit where as in 32 bit 8 bit for exponent and 23 bit for fraction that wht use more memory 
#! for 32bit-floating, number range -3e^38 to 3e^38
#! for 16bit-floating, number range -65504 to 65504
#! for bfloat16, number range -3e^38 to 3e^38 but memory reduce to 16 bit
#! for 8bit, number range -128 to 127 memory redice form 4 byte to 1 byte but dramestic loss of precision

#* to increase the performance of model : two ways 1) increase size of data 2) increase model params

#! when we should pretrain model from scrtach: when you have data vocabulary of that is not use in day to day life 
#! like medical ,science ,finance  for that need to train from scratch.

