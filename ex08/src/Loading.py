from tqdm import tqdm


def ft_tqdm(lst: range) -> None:
    # Using the generator function
    i = 0
    for i in tqdm(lst, total=len(lst), leave=True, unit='it'):
        yield
