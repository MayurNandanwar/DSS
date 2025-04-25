
#! Instruction fine tuning : base model pretrain on lot of data or information usually words , model knows about the 
#! things but doesnt know how to respond to our questions or prompt. so instructuion fine tuning helps it to be able to change 
#! its behaviour to be more helpful.

#! This method allow the model to generate the response that follows the given instructions. Here all model weights update so called full fine tuning
#! ex. classification/sentiment analysis, text generation, text summarization where we can instruct the model to generate completion 

#! In instruction fine tuning : you generate labeled-dataset, example how to summarize , how to responde answer 
#! with single shot or few shot example, this is how you ready the dataset and then split into train, validation and test
#! output of llm is probability distribution across the tokens. so we can compare the distribution of completion and that of training labels.
#!and use standard cross entropy function to calculate the loss between two token distribution and use that loss to update the weights in back propagation
#! we perform training for train dataset and then evaluat model using validation dataset this is how we can train model. this is called fine tuning or instruction fine tuning 


#* Finetune for single task:
#! fine tune the pretrained model for single task, with only 500-1000 example we can get the good performance 
#! potential downside of finetune on single task is, process may lead catastophic foirgetting means fine tuning 
#! increase models performance for specific task, and modifies the original weight so model forget how to do other task.
#! or can say degrade performance on other task.
#! when your need for llm for specific usecase, then catastrophic forgetting is not an issue 
#! but when your need from llm to perform multi task that time, fine tune the model with multi-task 
#! examples,good multitask fine tuning requires 50000-100000 example across many task,fine tune for multi-task this requires more data and computation as well (GPU)
#! and other option is to perform parameter efficient fine tuning (PEFT) : its a technique that  preserves weights of 
#! original llm and trains only task specific adapter layers(these adapter layers weights are fine tune for specific task) and parameters. PEFT shows great robustness to catastropic forgetting
#! since most of pretrained weight are unchanged


#* another finetuning method is PEFT(Parameter Efficient Fine Tunining):
#!main idea of this technique is to preserve the weight of the original LLM and trains only small number of task specific adapter layers and parameters
#! PEFT shows the greater robustness to catastrophic forgetting since most of the pretrained weights are left unchanged
#! Full Training of LLM is Computationally intensive,Full finetuning required memory not just store the model, but various other 
#! parameters required during training process. Even if your computer holds the models weight which are now on the order of hundeads of GB for 
#! largest model, you must also allocate the memory for optimizers, gradients,activations so its too hard to handle for computer hardware 
#! In contrast, PEFT method only updates the subset of parameters and remaining parameters are left unchanged.Using this technique very small 
#! number of weights like 15-20% of original parameters are updated during the training of model which makes memory 
#! requirement for model much manageable and also peft can often be perform in single GPU.

#! PEFT trade-off:
###! parameter efficiency
###! faster training speed
###! model performance
###! memory efficient
###! improves model quality for specific task

#* PEFT methods
#! 1st : selective methods: fine tune subset of original LLM parameters.in this you have option to train certain layers of the model 
#! 2nd : reparametrize parameters also work with the original LLM Parameters,but reduce the number of parameters to train by creating low rank transformation of the original network weights
#!        commonly used method method is LoRA(low rank adaption method)
#! 3rd :   1) additive methods carring out fine-tuning by keeping all the original weight frozen and introducing new trainable component
        #!    here there are two approaches : adapter method add new trainable layers to the architecture of the model in encoder and decpder layer 
        #!    after the attension and feed-forward layers
        #! 2) Soft Prompting(Prompt tuning with soft prompting) : keeps the models architecture fixed and frozen and focus on manupulating the input to achieve batter performace retraining the embedding weights


    #* LORA 
    #! --> step1: freeze all the weights of original LLM 
    #! --> step2: then, injecting 2 rank decomposition metrix alogside the original weights
    #! --> train the weights of this smaller metrics
    #! --> for inference, 2 low rank metrics are multiply togather to create metrix same dimension as frozen weights dimensions
    #!        then add in original weights and replace them in model with this updated value.now you can carry out specific task
    #! Researcher has found that applying lora to just self attension layer is often enough to fine tune for task and achieve performance 
    #! gain. Since most of the parameters are in the attension layers you get the biggest saving by applying LoRA to this weights metrics.
    #! ex. original transformers model have dimensions 512x64 
    #!     and let rank(r)=8 #--> smaller the range, low number of training params and memory consuption less.
    #!     then one of the low rank metrix will have dimension 512x8 and 
    #!      another one has 8x64, when perform dot product we get the original weight shape 512x64 
    #*        here we only train 4096 parametere using LoRA insread of 32,768.
    #! you can perform the task by Single GPU and can avoid the Distributed cluster of GPU
    #! since the rank decomposition metrix are small so you can so you can fine tune for different task and 
    #! switch them at time of inference by updating weights.
    #! we can use ROUGE to compare performance of fine tuned model to full finetune and originam model 

    #! prompt tuningng with soft prompt:
    #! it is completely different from prompt engineering, In prompt engineering you work with language to get your required completion.
    #!    ex. like you use few shot examples, goal is model to understand the task you want to crried out and to generate better completion.
            #! this requires lot of manual efforts and also limited by the length of the context window
    #! in this prompt tuning weights of LLM model are frozen,instead embedding vectors of soft prompts gets updated over time to optimize model's compeletion of the prompt. word closest with soft prompt token have similar meaning suggesting prompt learning word like representation
    #! in prompt tuning with soft prompt you add the additional trainable token to your prompt and leaving up to the supervised
    #!    learning process to determine thair values.set of trainable token is called as soft prompt and this gets prepended to the embedding vector 
    #!   that represent your input text.
    #! soft prompt have the same length as embedding vectors of input token
    #! 20-100 vertual token can be sufficient for good performance.
    #! vertual token can take any value and due to supervised learning process model learns the value for these vertual tokens that maximize performance of given task





#! RLHF(Re-inforcement Learning with human feedback)
#! -- > Because model trained on lots of internet data so possible that model can behave badly like can give Toxic words in response
#!      Aggrasive Response, provide dangerous information, also llm can mislead by providing incorrect answer.
#! Additional fine tuning with human feedback helps better align model with human preferance and to increase helpfulness,
#! honesty and harmlessness of completions
#! you can use RLHF to make sure that model produces the output that maximize the usefulness and relavance to the input prompt and minimize the potential for harm
#! yo can train the model to give caveates that acknowledge limitation and to avoid toxic language and topics.
#! model learns the preferences of each individual user through continuous feedback process

#* how RLHF works?
#!-->model learns to make decision related to specific task by taking action in an environment with objective is maximizing the reward received from action 
#! here generally model learn to make decision ,it received reward and penalty based on action it took. model try to 
#! goal of model is learn optimal policy to increase reward during training process
#! continuously learn from experience by taking action.
#! Action here is act of generating text. could be single word, sentence etc. depends on task