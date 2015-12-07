def main():
    f = open("testcases/ping_test.conf", "r")
    import measurement
    mq = measurement.Measurements()
    
    while True:
        counter = 0
        while counter < 10000000:
            counter += 1
    

if __name__ == "__main__":
    import os
    import sys
    sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    main()

