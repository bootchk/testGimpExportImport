
import logging

from gimpfu import *   # pdb and enums for mode conversions



"""
Understands how to down mode images, using PDB.
"""
class DownMode:

    logger = logging.getLogger("TestExportImport.DownMode")


    def to_BW(image, drawable):
        """ Return a new B&W image and drawable. """
        logger.info("Down moding to mode indexed B&W")
        # format requires indexed.  Convert to lowest common denominator: one-bit B&W mono
        # TODO convert only xbm to B&W, convert others to pallete
        new_image = pdb.gimp_image_duplicate(image)

        # convert seems to fail unless we flatten?
        pdb.gimp_image_flatten(new_image)

        # TODO defaults not working
        pdb.gimp_image_convert_indexed(new_image, DITHER_NONE, PALETTE_MONO, 0, False, False, "foo")
        new_drawable = pdb.gimp_image_get_active_layer(new_image)
        result = new_image, new_drawable
        return result


    def to_gray(image, drawable):
        """ Return a ne wgrayimage and drawable. """
        logger.info("Down moding to mode gray")
        new_image = pdb.gimp_image_duplicate(image)
        pdb.gimp_image_convert_grayscale(new_image)
        new_drawable = pdb.gimp_image_get_active_layer(new_image)
        result = new_image, new_drawable
        return result


    def to_sans_alpha(image, drawable):
        if pdb.gimp_drawable_has_alpha(drawable):
            logger.info("Down moding to sans alpha")
            new_image = pdb.gimp_image_duplicate(image )
            # flatten removes alpha channel
            pdb.gimp_image_flatten(new_image)
            new_drawable = pdb.gimp_image_get_active_layer(new_image)
            result = new_image, new_drawable
        else:
            # Unaltered
            result = image, drawable
        return result


    def to_16x16(image, drawable):
        logger.info("Down moding to 256 pixels, 16x16")
        # !!! 256 is the total, i.e. 16x16
        new_image = pdb.gimp_image_duplicate(image )
        pdb.gimp_image_scale(new_image, 16, 16)
        new_drawable = pdb.gimp_image_get_active_layer(new_image)
        result = new_image, new_drawable
        return result
