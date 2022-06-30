# Install Guide (Windows)

#### See [the requirements page](https://github.com/Dogey11/B3/blob/main/docs/windows/REQUIREMENTS.md) before continuing.


### Setup a BestBuy account if you haven't already. Make sure 2FA is DISABLED and that you only have one shipping address and payment method.


## Steps
* Download the script [here](https://github.com/Dogey11/B3/releases/latest/)

* Install dependencies:
    ```
    pip install -r requirements.txt
    playwright install
    ```

* Before first use, run it in verification mode:
    ```
    B3.py --verify
    ```
    * If you are using the minified version, replace ``B3.py`` with ``B3_min.py``.

* Follow prompts and let it run.
    * There is currently an [unresolved bug](https://github.com/microsoft/playwright/issues/9840) with Playwright and Firefox, you may get an error
    the first few times you run it.