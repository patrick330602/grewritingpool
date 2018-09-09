# Helper for GRE Writing Pool

Because why not?

## Install

`pip install grewritingpool`

or install from source:
`python3 setup.py install`

## Usage

Returned json by get_list():
```json
[
    {
        'type': <writing type>,
        'first': <first part of the question>,
        'second': <first part of the question, might not exist>,
        'instruc': <instruction>
    },
    ...
]
```

Returned json by get_random():
```json
{
    'type': <writing type>,
    'first': <first part of the question>,
    'second': <first part of the question, might not exist>,
    'instruc': <instruction>
}
```

As a API:
```python3
import grewritingpool as gwp
//returns a json list of arguments
list = gwp.get_list('arguement')
//returns a json of article from all article
list = gwp.get_random()
```

As a executable:
```bash
grewriting [all|issue|argument]
```

## License

MIT because I am lazy.