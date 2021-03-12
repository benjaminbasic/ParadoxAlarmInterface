
paradox = {}

# ARABIC

# map 0 to \x00
paradox['ar'] = [(0, 0),]

# map 1-32 to space
paradox['ar'][1:32] = [
    (x, 32) for x in range(1,33)
]

# windows-1251 from 33 to 127 equals to unicode
paradox['ar'][33:127] = [
    (x, x) for x in range(33,128)
]

# fill up from 128 to 255 with spaces
paradox['ar'][128:256] = [
    (x, 32) for x in range(128,256)
]

# replace some with space
for i in [63, 64, 91, 92, 93, 94, 95, 96] + list(range(123, 128)):
	paradox['ar'][i] = (i, 32)

# then there is a mix and match
paradox_extra_conversions = {
128:-56,
129:-54,
130:-53,
131:-52,
132:-51,
133:-50,
134:-45,
135:-44,
136:-43,
137:-42,
138:-41,
139:-40,
140:-39,
141:-38,
142:-31,
143:-30,
144:-29,
145:-28,
146:-27,
147:-26,
148:-22,
150:-57,
151:-49,
152:-48,
153:-47,
154:-46,
155:-25,
156:-24,
158:-28,
159:-55,
160:-23,
161:-56,
162:-54,
163:-53,
164:-52,
165:-51,
166:-50,
167:-45,
168:-44,
169:-43,
170:-42,
171:-41,
172:-40,
173:-39,
174:-38,
175:-31,
176:-30,
177:-29,
178:-28,
179:-27,
180:-26,
181:-22,
183:-56,
184:-54,
185:-53,
186:-52,
187:-51,
188:-50,
189:-45,
190:-44,
191:-43,
192:-42,
193:-41,
194:-40,
195:-39,
196:-38,
197:-31,
198:-30,
199:-29,
200:-28,
201:-27,
202:-26,
203:-22,
205:-56,
206:-54,
207:-53,
208:-52,
209:-51,
210:-50,
211:-45,
212:-44,
213:-43,
214:-42,
215:-41,
216:-40,
217:-39,
218:-38,
219:-31,
220:-30,
221:-29,
222:-28,
223:-27,
224:-26,
225:-22,
226:-58,
227:-57,
228:-49,
229:-48,
230:-47,
231:-46,
232:-25,
233:-24,
243:-61,
244:-61,
245:-59,
246:-59,
247:-60,
248:-60
}

# map to the 0-255 domain the signed ints
paradox_extra_conversions = { x: y+256*(0 if y>=0 else 1) for (x,y) in paradox_extra_conversions.items()}

for (b, c) in paradox_extra_conversions.items():
    if c >= 195: # map higher part of iso-8859-8 to unicode, starting from 0x0393
        c += 0x0623 - 195   

    paradox['ar'][b] = (b, c) # modify in the table

non_printable = [0, ]
needs_escape = [34, ] # "
