from gui import runUI
from data import init
from datastore import getData
def main():
    getData("8222")

    init()
    runUI()

if __name__ == "__main__":
    main()