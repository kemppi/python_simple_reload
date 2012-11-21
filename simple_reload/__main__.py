import logging
import traceback
from simple_reload import process_data as pd, load_data

_log = logging.getLogger(__name__)

def main():

    logging.basicConfig(level=logging.INFO, format='%(name)s: %(levelname)-8s %(message)s')

    data = load_data()
    _log.info("Data loaded.")
    while True:
        raw_input("Press enter to start a process cycle:\n")
        try:
            reload(pd)
        except NameError:
            _log.error("Could not reload the module.")
        try:
            pd.process_data(data)
        except Exception as e:
            _log.error("Caught exception from the process\n%s\n%s" % (e, traceback.format_exc()))

        _log.info("Cycle ready.")


if __name__ == "__main__":
    main()
