from pathlib import Path
import resize
from PIL import Image

# One bad gloop
# and she do what I yoinky
# Two big splurgs
# and a big ass gloopy
# Three more yoinks
# then I buy me a smoothie
# Poured up a gloop
# that's a gloop and a splurgy

# Developed by Ava!

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

# p = Path("emotes")
# for name in p.glob("*"):
#     image = Image.open(str(name))
#     print(image.size)

file_name = str(input("""
Please input the file name. 
Please note, if this file already exists the program will 
append to the end of the document.:
"""))

destruction_mode = bool(input("""
Would you like to enable UNSAFE mode?
This allows you to have the emotes path not one folder,
named emotes/ to remove from the image name.
This will ONLY WORK if there is only one folder,
such as emojis/, or images/.
This will NOT WORK if you have a path like emojis/images/.

True: Enable
False: Disable 
Case Sensitive
"""))

def solve_for_index(file):
    global file_name
    for name in file.glob("*"):

        if '.png' not in str(name):
            if '.gif' not in str(name):
                continue

        file = open(file_name, 'a')

        # if 'png' not in str(name):
        #     if 'gif' not in str(name):
        #         break

        file.write("""
        """)
        copy = str(name)
        copy = copy.replace(str(p), "")

        print(copy)


        print(copy, "is being used currently...")

        is_gif = copy.endswith('.gif')

        if is_gif:
            copy.replace('.gif', '')
        else:
            copy.replace('.png', '')

        file.write('{')
        file.write("""
            """)

        path_to_img = ''

        # if destruction_mode:
        #     for i in range(str(len(copy))):
        #         if copy[i] != '/':
        #             path_to_img += copy[i]


        copy = copy.replace(path_to_img, '')
        copy = copy.replace(".png", "")
        copy = copy.replace(".gif", "")
        file.write("\"name\": \"" + copy.replace(".png", "") + '",')
        file.write("""
            """)

        if is_gif:
            file.write('"type": \".gif\"')
        else:
            file.write('"type": \".png\"')
        file.write("""
        """)

        file.write("},")

        print(copy)
        file.close()

        # if 'gif' in str(name):
        #     break
        # else:
        resize.resizeimage(str(name))





def solve(p):
    solve_for_index(p)
    for name in p.glob("*"):
        if '.' not in str(name):
            new_p = Path(str(name))
            # print(str(name))
            # print(str(new_p))
            solve_for_index(new_p)
            solve(new_p)


p = Path("testt")
# solve_for_index(p)
solve(p)


print("""


""")


print("The operation completed successfully, and was saved to:", file_name)