# Copyright 2020 Miki Tebeka <miki@353solutions.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import re
from collections import defaultdict


def word_freq(text, freqs=defaultdict(int)):
    """Calculate word frequency in text. freqs are previous frequencies"""
    for word in [w.lower() for w in re.findall(r'\w+', text)]:
        freqs[word] += 1
    return freqs


freqs1 = word_freq('Duck season. Duck!')
freqs2 = word_freq('Rabbit season. Rabbit!')
print(freqs1)
print(freqs2)
