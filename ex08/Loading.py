from tqdm import tqdm


def ft_tqdm(lst: range) -> None:
    """ yield is used in a function to make it a generator.
    Instead of returning a value and ending the function,
    yield produces a value and pauses the function, saving its state
    for future use.
    - yield turns a function into a generator.
    - It pauses the function and returns a value each time it’s called.
    - The function’s state is saved between calls.
    - Useful for memory-efficient, stateful iteration over large
    or infinite sequences. """
    i = 0
    for i in tqdm(lst, total=len(lst)):
        yield
    # iterable, total or nb of expected iterations,
    # leave : [default: True], keeps all traces of the
    # progressbar upon termination of iteration. If None,
    # will leave only if position is 0.
    # unit=it by default
