from os import PathLike
from pathlib import Path

# One bad gloop
# and she do what I yoinky
# Two big splurgs 
# and a big ass gloopy
# Three more yoinks
# then I buy me a smoothie
# Poured up a gloop
# that's a gloop and a splurgy


# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
# IN NO EVENT SHALL THE AUTHORS BE LIABLE FOR ANY CLAIM, DAMAGES OR
# OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE,
# ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
# OTHER DEALINGS IN THE SOFTWARE.

file_name = str(input("Please input json output name: (Leave blank for input.json)"))


def solve_for_index(path):
    global file_name
    for name in path.glob("*"):

        if file_name == '':
            file_name = 'index.json'

        file = open(file_name, 'a')

        file.write("""
        """)

        copy = str(name)
        copy = copy.replace(str(p), "")

        is_gif = copy.endswith('.gif')

        if is_gif:
            copy.replace('.gif', '')
        else:
            copy.replace('.png', '')

        file.write('{')
        file.write("""
            """)
        copy = copy.replace('Copy_Emotes/', '')
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

        print("Successfuly wrote", copy, "to", file_name)
        file.close()


# def solve(path):
#     for name in path.glob("*"):
#         #if '.png' and '.gif' not in str(name):
#          #   print(False)
#         #else:
#             new_p = Path(str(name))
#             print(str(name))
#             print(str(new_p))
#
#             solve_for_index(p)
#             solve(new_p)


p = Path("emoji/Emojis_bread_cats_cat_corner")
solve_for_index(p)

print("Successfully written json file with name:", file_name)
