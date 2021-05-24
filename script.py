from pathlib import Path
import resize

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


file_name = str(input("""
Please input the file name. 
Please note, if this file already exists the program will 
append to the end of the document.:
"""))


def solve_for_index(file):
    global file_name
    for name in file.glob("*"):
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
        copy = copy.replace('emotes/', '')
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
    for name in p.glob("*"):
        if '.' not in str(name):
            new_p = Path(str(name))
            # print(str(name))
            # print(str(new_p))
            solve_for_index(new_p)
            solve(new_p)


p = Path("")
# solve_for_index(p)
solve(p)


print("""


""")


print("The operation completed successfully, and was saved to:", file_name)