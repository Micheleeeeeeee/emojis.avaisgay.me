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


def solve_for_index(p):
    
    for name in p.glob("*"):
        file = open('index.json', 'a')

        file.write("""
        """)
        copy = str(name)
        copy.replace("emotes/", "")

        copy.replace('emotes/', '')

        print(copy)
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

from os import PathLike
from pathlib import Path

p = Path("intj")

solve_for_index(p)
