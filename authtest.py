import redis
import sys, getopt
__author__='tangna'


#print sys.argv

opts, args = getopt.getopt(sys.argv[1:],"ha:")
app_id = ""


redis_db= {"host":"10.0.8.199", "port":"6383", "db":3}


def authtest(app_id):
    r = redis.Redis(**redis_db)
    print r.hgetall("AD_BDP_SENSEAR_AUTH_COUNT:{0}".format(app_id))
    print r.hgetall("AD_BDP_SENSEAR_INTERNAL_AUTH_COUNT:{0}".format(app_id))

if __name__ == "__main__":
    for opt, arg in opts:
        if opt == '-h':
            print sys.argv[0], " -a <app_id>"
        elif opt == '-a':
           authtest(arg)
            
