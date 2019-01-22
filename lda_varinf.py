# Code for LDA-Variational Inference
# Sandeep Shetty - 1.18.19
# Pseudocode followed from Blei et al (2003)
# Status - figuring it out (v1)



'''

*** Input 
 Term list
 Number of topics - k 
 Raw-word-matrix (not unique words) - wordDocMat
 Tolerance values - tol

*** Output
 LDA paramters - Beta (probability..)

'''

# For each document
for doc in range(len_d):

# create empty 2-D matrix for holding 'phi' (document-word-topic)
# create empty 2-D array for 'gamma' (document-topic)

    pi_tk = np.empty(shape=[len_t,k],dtype=np.int)
    gamma_dk = np.empty(k,dtype=np.int)

    dLength = wordDocMat[:,doc].sum()  #Length of the selected document

#INITIALIZATION
    # Intialize parameter "phi" in word-topic model for each document

    phi = 1./k

    # generate assignment (z_{d,n})
    for index, val in enumerate(wordDocMat[:,doc]):
        if  val!= 0:
            pi_tk[index,:] = np.random.multinomial(1,phi*k) 
        else:
            pi_tk[index,:] = 0 

    # Intialize "gamma" in per topic  for each document

    gamma_k = alpha + dLength/k

    # pre-calculate some terms
    docWord = [w for w in wordDocMat[:,doc] if w != 0] #words in document 
    setdocWord = list(set(docWord)) # unique words
    #countDocWord = [
    len_docu = len(docWord) # length of document selected

#ITERATION
    while diff>0.001:
        for index,word in enumerate(wordDocMat[:,doc]):
            if word!=0:
                countWordinDoc = wordDocMat([index,doc]) # N_w calculate beta_ij =
                
                prb_ij = []
                for i in range(k):
                    beta_ij = 0 # 'w' with topic 'i'
                    
                    for nindex in range(len(pi_tk.shape[0])):
                        if pi_tk[nindex,k]==1 and termClean[nidnex] == word:
                            beta_ij += 1

                    sumTopic = np.sum(pi_tk, axis = 0) # topic 'i' assigned in doc
                    
                    # Prob(wn=w|zn=i)
                    prb_ij.append((beta_ij/countWordinDoc)/(sumTopic/len_docu)) #
                
            psi_n[index,k]=prb_ij/prb_ij.sum()  #need to define psi_n  
        
        newgamma = alpha + psi_n.sum(axis=0)
        diff = gamma_k - newgamma
        gamma_k = newgamma # reassign


#Beta - the probability of the observed word at location 't' given that that the topic
#is 'i' -- beta_ik. Once we have the assignment then we can empirically
#calculate that term for each update
# word list
# doc-word matrix 
# count of word in the document



