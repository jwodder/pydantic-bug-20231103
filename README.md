This is an MVCE for a bug in [Pydantic](https://github.com/pydantic/pydantic)'s
mypy plugin in which a false positive is generated for
`warn_required_dynamic_aliases` on properties & validators when
`alias_generator` set.

To use this MVCE, install [hatch](https://hatch.pypa.io) and run `hatch run
typing:check`.

The bug report is at <https://github.com/pydantic/pydantic/issues/8008>.
