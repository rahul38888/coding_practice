import click


@click.group()
def cli():
    pass


@click.command(help="print welcome message multiple times")
@click.option("-c", "--count", default=1, show_default=True, type=click.INT)
@click.argument("name", type=click.STRING)
def names(name: str, count: int):
    """
    python.exe test.py names --count=2 Rahul
    """
    for i in range(count):
        click.echo(f"{i + 1}. Welcome {name}!")


@click.command(help="Add two numbers")
@click.option("-n", "--numbers", type=click.FLOAT, nargs=2, help="Two numbers to be added")
def add(numbers: list[int]):
    """
    python.exe test.py add -n 1 2 3 4
    """
    click.echo(f"{" + ".join(map(lambda n: str(n), numbers))} = {sum(numbers)}")


@click.command(help="Multiply multiple numbers")
@click.option("-n", "--numbers", type=click.FLOAT, multiple=True, help="Multiple numbers to be multiplied")
def multiply(numbers: list[int]):
    """
    python.exe test.py multiply -n 1 -n 2 -n 3 -n 4
    """
    ans = 1
    for n in numbers:
        ans *= n
    click.echo(f"{" x ".join(map(lambda n: str(n), numbers))} = {ans}")


@click.command(help="Register person in database", name="person")
@click.option("-p", "--person", type=click.Tuple([click.STRING, click.INT]), help="Person info in order <Name> <Age>")
def add_person(person):
    """
    python.exe test.py person -p Rahul 31
    """
    name, age = person
    click.echo(f"Added person entry into database, entry = Person[name={name}, age={age}]")


@click.command(help="Level of verbosity ")
@click.option("-v", "--verbose", count=True, help="Level of verbosity")
def verbosity(verbose: int):
    """
    python.exe test.py verbosity -vv

    Verbosity = 2
    """
    click.echo(f"Verbosity = {verbose}")


@click.command(help="Take names", name="take_name")
@click.option("--greeting", is_flag=True, help="Include greetings before name")
@click.option("-n", "--name", default="rahul", type=click.STRING, help="Name")
def take_name(name: str, greeting: bool):
    """
    python.exe test.py take_name --greeting -n Ram

    Hey Ram
    """
    if greeting:
        name = "Hey " + name
    click.echo(name)


@click.command(help="Transform name", name="change_name")
@click.option("--upper", "change", flag_value="upper", default=True, help="Uppercase name")
@click.option("--lower", "change", flag_value="lower", help="Lowercase name")
@click.option("-n", "--name", default="Rahul", show_default=True, type=click.STRING, help="Name")
def change_name(name: str, change: str):
    """
    python.exe test.py take_name --upper -n ram

    RAM
    """
    click.echo(getattr(name, change)())


cli.add_command(names)
cli.add_command(add)
cli.add_command(add_person)
cli.add_command(multiply)
cli.add_command(verbosity)
cli.add_command(take_name)
cli.add_command(change_name)

if __name__ == '__main__':
    cli()
