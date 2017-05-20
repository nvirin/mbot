import subprocess
import sys
import json
import time

setOfTags = set()
setOfTags.add(sys.argv[1])


# for _ in range(int(sys.argv[2])):
def search():
    tmpNextSet = setOfTags.copy()
    while (True):
        # 1
        for tag in tmpNextSet:
            relatedTags = subprocess.check_output(["php", "phpapi/test.php", tag])
            arrayOfTags = str.split(relatedTags)
            for element in arrayOfTags:
                setOfTags.add(element)
                percentage = ((float(setOfTags.__len__()) / float(sys.argv[2])) * 100)
                print("Status: " + "{:.0f}".format(percentage) + "%  -  " + str(setOfTags.__len__()) + "/" + str(
                    sys.argv[2]) + " Hashtags")
                if setOfTags.__len__() >= int(sys.argv[2]):
                    print('Done')
                    return
                sys.stdout.write("\033[F")
                # 5 +1
            tmpNextSet = setOfTags - tmpNextSet

            # tmpNextSet = bla.copy()
            # 5


search()

print('Result: ' + str(setOfTags))


class SetEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, set):
            return list(obj)
        return json.JSONEncoder.default(self, obj)

with open('related.json', 'w') as f:
    json.dump(setOfTags, f, cls=SetEncoder)
