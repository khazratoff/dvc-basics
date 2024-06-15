# EPAM-MLE. Module7. Data Governance.

1. Clone the repo:
```bash
git clone https://github.com/khazratoff/dvc-basics.git
cd dvc-basics
```
2. Create virtual environment and activate:
```
python -m venv dvc-env
source dvc-env/bin/activate
```
3. Install dependencies:
```
pip install -r requirements.txt
```
4. Get data:
```
dvc pull
```
5. Reproduce data pipelines and experiments:
```
dvc repro
```
6. Get metrics:
```
dvc metrics show
```