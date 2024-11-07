def callLimit(limit: int):

    """decorator maker"""

    count = 0

    def callLimiter(function):

        """decorator"""

        def limit_function(*args: any, **kwds: any):

            """wrapper"""

            nonlocal count

            if count < limit:
                count += 1
                return function()
            print(f"Error: {function} call too many times")
            return

        return limit_function

    return callLimiter
