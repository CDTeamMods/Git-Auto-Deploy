
import os
import logging
from filelock import FileLock, Timeout

class Lock():
    """Simple implementation of a mutex lock using filelock."""

    path = None
    lock = None
    _owned = False

    def __init__(self, path):
        self.path = path
        self.lock = FileLock(path)
        self._owned = False

    def obtain(self):
        logger = logging.getLogger()

        try:
            self.lock.acquire(timeout=0)
            self._owned = True
            logger.debug("Successfully obtained lock: %s" % self.path)
        except Timeout:
            return False

        return True

    def release(self):
        logger = logging.getLogger()

        if not self.has_lock():
            raise Exception("Unable to release lock that is owned by another process")

        self.lock.release()
        self._owned = False
        logger.debug("Successfully released lock: %s" % self.path)

    def has_lock(self):
        return self._owned

    def clear(self):
        import logging
        import os
        logger = logging.getLogger()

        if os.path.exists(self.path):
            try:
                os.remove(self.path)
            except OSError:
                pass
            
        # Also release internal state if we owned it
        if self._owned:
            self.lock.release()
            self._owned = False

        logger.debug("Successfully cleared lock: %s" % self.path)
