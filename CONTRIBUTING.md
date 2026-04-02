# Contributing

Thanks for checking this out. If you want to contribute:

1. Fork the repo
2. Create a branch (`git checkout -b feature/your-algorithm`)
3. Add your implementation in both Python and JavaScript if possible
4. Include tests and Big O analysis in the docstring/comment
5. Make sure all existing tests still pass
6. Open a PR

## Guidelines

- Keep implementations readable — this is a learning resource, not a code golf contest
- Add Big O analysis (time and space) at the top of each file
- Tests should cover at least: basic case, empty input, single element, edge cases
- Follow the existing naming conventions (snake_case for Python, camelCase for JS)

## Running Tests

```bash
# Python
cd python
pytest tests/ -v

# JavaScript
cd javascript
npm install
npm test
```
