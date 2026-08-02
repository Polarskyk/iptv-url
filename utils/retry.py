from time import sleep

from utils.i18n import t

max_retries = 2


def retry_func(func, retries=max_retries, name="", retry_delay=1.0):
    """
    Retry the function.
    The first attempt runs immediately; only retries are rate-limited by retry_delay.
    """
    for i in range(retries):
        try:
            return func()
        except Exception as e:
            if name and i < retries - 1:
                print(t("msg.failed_retrying_count").format(name=name, count=i + 1), flush=True)
            elif i == retries - 1:
                raise Exception(
                    t("msg.failed_retry_max").format(name=name)
                )
            if retry_delay > 0:
                sleep(retry_delay)
    raise Exception(t("msg.failed_retry_max").format(name=name))
