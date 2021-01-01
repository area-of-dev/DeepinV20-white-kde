import os
import sys
import glob
import optparse
from cairosvg import svg2png

from multiprocessing import Pool


def excluded(source=None, ignores=[]):
    for pattern in ignores:
        if source.find(pattern) == -1:
            continue
        return True
    return False


def colorify(source=None, color='#3498db',ignores=[]):
    if not os.path.exists(source):
        return None

    with open(source, 'r+') as stream:
        if excluded(source, ignores):
            return stream.read()

        content = stream.read()
        content = content.replace('#53b7ec',color)
        content = content.replace('#3daee9',color)
        return content

    return None


def pngify(source=None, destination=None, size=None):
    if source is None: return False
    if destination is None: return False
    if size is None: return False

    try:

        width, height = size

        with open(source, 'rb') as stream:
            svg2png(bytestring=stream.read(), unsafe=True,
                    write_to=destination,
                    output_width=width,
                    output_height=height)
            stream.close()

    except Exception as ex:
        print(source, destination, ex)

    return True


def iconify(arguments=None):
    scalable, options, size = arguments
    width, height = size

    assert(os.path.exists(options.destination))
    assert(os.path.exists(options.source))

    pattern = [
        '/vendors/',
    ]

    destination_scalable = os.path.dirname(scalable)
    destination_scalable = destination_scalable.replace(options.source, options.destination)    
    if not os.path.exists(destination_scalable):
        os.makedirs(destination_scalable, exist_ok=True)

    destination_fixedsize = os.path.dirname(scalable)
    destination_fixedsize = destination_fixedsize.replace('scalable/', '{}x{}/'.format(width, height))    
    # if not os.path.exists(destination_fixedsize):
    #     os.makedirs(destination_fixedsize, exist_ok=True)

    print('.', end='')

    scalable_folder = os.path.dirname(scalable)

    destination_file1 = os.path.basename(scalable)
    destination_file1 = "{}/{}".format(destination_scalable, destination_file1)

    destination_file2 = os.path.basename(scalable)
    destination_file2 = "{}/{}".format(destination_scalable, destination_file2)    

    destination_file3 = os.path.basename(scalable)
    destination_file3 = destination_file3.replace('.svg', '.png')
    destination_file3 = "{}/{}".format(destination_fixedsize, destination_file3)    

    destination_file1_content = colorify(scalable, options.color, pattern)
    if destination_file1_content and len(destination_file1_content):
        with open(destination_file1, 'w') as stream:
            stream.write(destination_file1_content)
            stream.close()

    if destination_file2.find('symbolic') == -1:
        if not options.nopng:
            pngify(scalable, destination_file3, size)

        if options.nosymbolic:
            return None

        destination_file2 = destination_file2.replace('.svg','-symbolic.svg')
        destination_file2_content = colorify(scalable, options.color, pattern)
        if destination_file2_content and len(destination_file2_content):
            with open(destination_file2, 'w') as stream:
                stream.write(destination_file2_content)
                stream.close()



if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("--file", default=None, dest="file", help="file to parse")
    parser.add_option("--destination", default=None, dest="destination", help="icon destination path")
    parser.add_option("--source", default=None, dest="source", help="icon source path")
    parser.add_option("--color", default="#3498db", dest="color", help="icon source path")
    parser.add_option("--skip-symbolic", default=False, dest="nosymbolic", help="do not generate symbolic icons")
    parser.add_option("--skip-png", default=True, dest="nopng", help="do not generate png icons")

    (options, args) = parser.parse_args()

    assert(os.path.exists(options.destination))
    assert(os.path.exists(options.source))

    elements = []

    pattern = '{}/**/*.svg'.format(options.source)
    for source in glob.glob(pattern, recursive=True):
        if os.path.isdir(source):
            continue

        elements.append((source, options, (8, 8)))
        elements.append((source, options, (12, 12)))
        elements.append((source, options, (16, 16)))
        elements.append((source, options, (20, 20)))
        elements.append((source, options, (24, 24)))
        elements.append((source, options, (32, 32)))
        elements.append((source, options, (48, 48)))
        elements.append((source, options, (64, 64)))
        elements.append((source, options, (96, 96)))
        elements.append((source, options, (128, 128)))
        elements.append((source, options, (256, 256)))
        elements.append((source, options, (512, 512)))

    pool = Pool(processes=4)
    pool.map(iconify, elements)
    pool.close()
