from Crowd import PersonCrowd

if __name__ == '__main__':
    pc = PersonCrowd.PersonCrowd()
    for i in range(1000):
        print("Iteration:{}".format(i))
        assert isinstance(pc.iteration, object)
        pc.iteration()
    pc.summary()
    print("END!")