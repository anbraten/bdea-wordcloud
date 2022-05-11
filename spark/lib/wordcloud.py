import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_gradient_magnitude
from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
import os
import os.path

basePath = os.path.join(os.getcwd(), 'fake-hdfs')

def generate_wordcloud(filename: str, frequencies):
    print("generating wordcloud ...")

    # load image. This has been modified in gimp to be brighter and have more saturation.
    parrot_color = np.array(Image.open(os.path.join(basePath, 'parrot.jpg')))
    # subsample by factor of 3. Very lossy but for a wordcloud we don't really care.
    parrot_color = parrot_color[::3, ::3]

    # # create mask  white is "masked out"
    parrot_mask = parrot_color.copy()
    parrot_mask[parrot_mask.sum(axis=2) == 0] = 255

    # some finesse: we enforce boundaries between colors so they get less washed out.
    # For that we do some edge detection in the image
    edges = np.mean([gaussian_gradient_magnitude(parrot_color[:, :, i] / 255., 2) for i in range(3)], axis=0)
    parrot_mask[edges > .08] = 255

    # create wordcloud. A bit sluggish, you can subsample more strongly for quicker rendering
    # relative_scaling=0 means the frequencies in the data are reflected less
    # acurately but it makes a better picture
    wc = WordCloud(max_words=2000, mask=parrot_mask, max_font_size=40, random_state=42, relative_scaling=0, min_word_length=4)
    # wc = WordCloud(max_words=2000, max_font_size=40, random_state=42, relative_scaling=0, min_word_length=4)

    # generate word cloud
    wc.generate_from_frequencies(frequencies)

    # create coloring from image
    image_colors = ImageColorGenerator(parrot_color)
    wc.recolor(color_func=image_colors)
    plt.figure(figsize=(10, 10))

    print("wordcloud generated")

    svg = wc.to_svg()

    print("wordcloud rendered")

    f = open(filename, "w")
    f.write(svg)
    f.close()

    print("wordcloud saved to: "+filename)
