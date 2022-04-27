import matplotlib.pyplot as plt
import matplotlib.image as mplim
import numpy as np


# Read sky cam data
filename = '../../../swirlldata/swirlldata2020_0308_082700.jpg'
img_orig = mplim.imread(filename)

# Date extraction
raw_date = filename.split("/")[-1]
img_date = raw_date[-20:]

# Limit image to sky
img_orig = img_orig[:,0:1300,:]


##########################
# Compute cloud fraction #
##########################
img = np.int16(img_orig)  # Convert image to 16-bit signed int for computation
cf_img = img[:,:,2] - img[:,:,0]  # Get different between blue and red
cf_img = np.where(cf_img < 0, -cf_img, cf_img)  # Absolute value of difference
cf_img = np.uint8(cf_img)  # Convert back to 8-bit unsigned integer

# Get number of pixels above threshold percentage
threshold_percentage = 0.10  # approx 20% experimentally observed
threshold_img = (cf_img / 255) > threshold_percentage
thresh_vals = np.count_nonzero( (cf_img / 255) > threshold_percentage )

# Calculate cloud fraction in oktas
cf_okta = 8 - int( ( thresh_vals / cf_img.size ) * 8 )

# Convert cloud fraction to named cloud cover
cf_names = {
       0 : "CLR",
       
       1 : "FEW",
       2 : "FEW",
       
       3 : "SCT",
       4 : "SCT",
       
       5 : "BKN",
       6 : "BKN",
       7 : "BKN",
       
       8 : "OVC"
       }

cf_name = cf_names[cf_okta]



###############
# Plot Images #
###############

# Plot configuration
color = "Blues"
fig, ax = plt.subplots(nrows = 2, sharex = True, figsize = [10, 5], constrained_layout = True)

# Show cloud fraction computation
fig.suptitle(("Total Cloud Fraction: " + str(cf_okta) + "/8 or " + cf_name), fontsize = 16)
# fig.title("Date: " + )

# Plot "sky"
threshold_img = threshold_img.transpose()
ax[0].imshow(threshold_img, cmap = color)
ax[0].axis("off")
ax[0].set_title("\"Blue Sky\" Characterization")

# Plot standard image
rgb_image = np.swapaxes(img_orig, 0, 1)
ax[1].imshow(rgb_image, cmap = color)
ax[1].axis("off")
ax[1].set_title("Raw Image")

plt.show()