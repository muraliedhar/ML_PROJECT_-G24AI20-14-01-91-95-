#  Hand Gesture Recognition Using SVM

This project implements a static hand gesture recognition system using computer vision and machine learning techniques, specifically the Support Vector Machine (SVM) classifier.

##  Project Summary

We developed a vision-based model that classifies hand gestures corresponding to alphabetic characters (A–F). The system uses a Bag-of-Visual-Words (BoVW) model for image representation and an SVM for classification.

##  Technologies & Tools
- Python
- OpenCV
- scikit-learn
- NumPy
- SIFT (Scale-Invariant Feature Transform)
- Canny Edge Detection
- MiniBatch KMeans (for clustering)

##  File Descriptions

- **`hand_gesture_svm.py`**  
  Main script that loads images, extracts SIFT descriptors, builds BoVW histograms, trains and tests the SVM classifier.

- **`surf_image_processing.py`**  
  Contains `func()` and `func2()` for preprocessing images and extracting SIFT or ORB descriptors.

- **`test.py`**  
  Checks OpenCV version and SIFT availability.

- **`submission_surf_svm.csv`**  
  Stores SVM predictions and true labels for performance evaluation.

- **`output.txt.txt`**  
  Log file containing image paths and possible descriptor counts (for debugging or analysis).

##  How It Works

1. **Preprocessing**:  
   - Resize image  
   - Segment skin region using HSV color space  
   - Apply Canny edge detection

2. **Feature Extraction**:  
   - Use SIFT to detect and describe keypoints

3. **BoVW Model**:  
   - Cluster all descriptors with MiniBatch KMeans (150 clusters)  
   - Represent each image as a histogram of visual words

4. **Classification**:  
   - Train an SVM with linear kernel on BoVW histograms  
   - Evaluate using accuracy, precision, recall, and F1-score

##  Results

The SVM classifier showed strong performance across all gesture classes. The system is efficient, scalable, and adaptable for real-time or larger gesture datasets.

##  Future Work

- Extend to dynamic gesture recognition  
- Integrate real-time webcam input  
- Use deep learning models (e.g., CNN) for enhanced accuracy

## 📬 Contact

**Author**: Muraliedhar Kanchibhotla,Arpit tomar , pallavi sarangi ,vikrant
**Institution**: IIT Jodhpur
**Email**:g24ai2014@iitj.ac.in, g24ai2001@iitj.ac.in,g24ai2091@iitj.ac.in , g24ai2095@iitj.ac.in
