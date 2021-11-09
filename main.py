import cv2   

# Loading base image and template image using imread()
img = cv2.imread(r'D:\projects\AI-ML-MINI-PROJECT-2\Pratham\images\wheres_waldo.jpg')
# Coverting 'img' into grayscale
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
template = cv2.imread(r'D:\projects\AI-ML-MINI-PROJECT-2\Pratham\images\temp.jpg',0)
h ,w = template.shape #Getting the height and width of the template image

# Using 'cv2.matchTemplate' method for comparing Template with base image 
match = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.99

# Using 'cv2.minMaxLoc' method for finding the max_location where templeate matches Base image
min_val, max_val, min_location, max_location = cv2.minMaxLoc(match)
location = max_location
font = cv2.FONT_HERSHEY_PLAIN

"""
location[0] + w, location[1] + h
Here 'w' is weight of template and 'h' is height of template
used to mark the mached area
"""
cv2.rectangle(img, location, (location[0] + w, location[1] + h), (0,0,255), 2)
cv2.putText(img,"Waldo Spotted.", (location[0]-40,location[1]-5),font , 1, (0,0,0),2)

cv2.imwrite('AI-ML-MINI-PROJECT-2\Pratham\grayscale.jpg',img_gray)
cv2.imshow('grayscale.jpg',img_gray)
cv2.imwrite('AI-ML-MINI-PROJECT-2\Pratham\Results.jpg',img)
cv2.imshow('Results.jpg',img)

# to wait until any key is pressed
cv2.waitKey(0)
# using 'cv2.destroyAllWindows()' method to destroy all windows whenever any key is pressed
cv2.destroyAllWindows()