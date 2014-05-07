# import json

# tag_cloud_file = open('tag_cloud.json', 'r+')
# tag_cloud_csv_file = open('tag_cloud.csv', 'w+')
# tag_cloud = json.load(tag_cloud_file)
# for tag in tag_cloud:
#     tag_cloud_csv_file.write('%(text)s, %(size)s\n' % tag)

# tag_cloud_csv_file.close()


import random
charecters = ["A","B","C","D","E","F","G","H","I","J","K", "L", "M", "N"]

for index in xrange(20):
    print [random.choice(charecters) for x in xrange(3)]


from pymarkovchain import MarkovChain
mc = MarkovChain("./markov")
mc.generateDatabase("a b c")