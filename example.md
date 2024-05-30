*  Federated Learning is a way to train AI models without anyone seeing or touching your data.
- Today's Data is moving towards **A Decentralized Manner** .
- The newer AI Models are trained collaboratively on the edge, on the data which doesn't leave your device.
## Introduction and History

*  Google coined this term in 2016 ,at the time where misuse of user data was a hot-topic.
* The main credit goes to Nathalie Baracaldo(Now Head of IBM's AI Privacy and security), who was then pursuing his PhD, mentioned this term in his landmark paper. 
## Importance of Federated Learning

* **Privacy** : Instead of data being sent to a centralized server, FL allows for training to occur locally on the edge device, preventing data breaches.

* **Data Security** : Only Encrypted Model Updates are shared with the central server. Additionally, secure aggregation techniques like [**Secure Aggregation Principle**](https://research.google/pubs/practical-secure-aggregation-for-federated-learning-on-user-held-data/#:~:text=Secure%20Aggregation%20is%20a%20class,their%20private%20value%20except%20what) allow the decryption of only aggregated results .

* **Access to Heterogenous Data** : FL guarantees access to data spread across multiple devices, locations and organizations, making it possible to train models on sensitive data, like financial and healthcare, while maintaining privacy and security. Due to this the models are more generalizable and can be used for other purposes.
## How does Federated Learning work?

* A generic baseline model is stored at central server. The copies of this model are shared to the client devices , which trains the model on local data of the user using the device . 
* Overtime, these models the models on individual devices become personalized to the user of the device and provide a better user experience.
* In the next stage, updates from locally trained models are shared with the main model located at the central server using secure aggregation techniques.
* The model , then combines and averages different inputs to generate new learnings. This makes the model more generalized.
* After being trained with the new parameters, it's shared with the client devices again for the next iteration.
* With each iteration the model gathers various information and improve further without creating privacy breaches.
![[63dd0b6a89a72c6743b46b09_federated learning 2.webp]]


## Types of Federated Learning

* There are three types of FL.
		
1. Centralized Federated Learning: 
			- It requires a central server, which co-ordinates the selection of client devices in the beginning and gathers the model updates during training.
			- The Communication happens only between the central server and the edge devices.
			- This model poses a bottleneck problem, where network failures can halt the process.
			- ![[63dd0bbd5a5e3b2accccdc3f_federated learning 1.webp]]
2. Decentralized Federated Learning:
		-  Doesn't require a central server to co-ordinate the learning. Instead model updates are shared only among the interconnected edge devices.
		- The final model is obtained on an edge device by aggregating the local updates of the connected edge devices.
		- Prevents the possibility of a single point failure.
		- Accuracy depends on the network topology of edge devices.
		- ![[63dd0be289a72c7e01b470ef_local model.webp]]
3. Heterogenous Federated Learning:
		- Involves including heterogenous clients such as mobile phones, computers or IoT devices. These devices differ in hardware, software and computation capabilities.
		- Happens very rarely in real-world. to assume the local models' attributes resemble that to of the main model.

## Federated Learning Algorithms

1. Federated stochastic gradient descent (FedSGD) :
		-  Regular Stochastic GD assumes data in mini-batches(fraction of whole data)
		-  In terms of FL , the mini batches can be considered  different client devices that comprise local data.
		- Central Model is distributed to the clients , and each client computes the gradients using the local data.
		- These gradients re then passed to the central server, which aggregates the gradients in proportion to the number of samples present on each client to calculate the gradient descent step.
2. Federated Averaging (FedAvg):
		- Extension of FedSGD Algorithm (Generalized form of FedSGD).
		- Clients can perform more than one local gradient descent update.
		- Instead of sharing the gradients with the central server, weights tuned on local model are shared.
		- Finally the server aggregates the clients' weights.
		- If all the clients begin from same initialization, averaging the gradients is equal to averaging the weights.
		- Federated Averaging leaves room for tuning the local weights before sending them to the central server for averaging.
3. Federated Learning with dynamic regularization(FedDyn):
		-  Regularization in machine learning methods aims to add a penalty to the loss function to improve the generalizability of the model.
		- In FL , the final and global loss of the central model is calculated based on local losses generated from heterogenous devices.
		- FedDyn method aims to generate regularization term for local losses by adapting to the data statistics, such as amount of the data or communication cost.
		- This modification of local losses through dynamic regularization enables local losses to converge to global loss.

## Challenges and limitations of Federated Learning
1. Communication Efficiency: 
		 - The transfer of messages becomes slow due to several reasons : low bandwidth ,lack of resources or geographical location.
		 - To them efficient , the total number of message passes and the size of a message in a single pass should be reduced . 
		 - It can be achieved using
			- Local Updating (reduce number of rounds)
			- Model Compression (To reduce the size of the message)
			- Decentralized Training(to operate on low bandwidth)
2. Privacy:
		- Although the local data stays on the user device, there's a risk for the information to be revealed from the model updates shared in the central network.
		- Privacy Preserving Techniques include:
			- Differential Privacy : Adding Noisy Data that makes it difficult to discern real information in case of data leaks.
			- Homomorphic Encryption : Performing Computation on encrypted data.
			- Secure multiparty computation : 
				- Spread the sensitive data to different data owners so that they can collaboratively perform computation and reduce the risk of privacy breach.
3. System Heterogeneity: 
		- With large number of devices playing a role in FL Topology Network, accounting for differences in storage, communication and computational capabilities is a huge challenge. Additionally only a few devices participating at a given time , lead to biased training.
		- These can be handled by the techniques of asynchronous communication, active device sampling and fault tolerance.
4. Statistical heterogeneity:
		- This problem occurs when multiple variations of data present across the client devices.(Like Quality and Geographic location of the data)
		- That means that data is non -i.i.d in a federated learning setting , which in contrast with assumption that i.i.d data in normal algorithms.
		- This causes problems in data structuring, modeling, and inferencing phases.

## Real Life Application of FL in Medical and Healthcare Industry

- With Federated learning ,models can be trained through secure access to data from patients and medical institutions while data remains at its original premises.
- This helps many institutions to collaborate with others and make it possible for models to learn from more datasets securely.
- 
![[63dd0c560c58c700a5ff6423_federated learning in healthcare.webp]]
