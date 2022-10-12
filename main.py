## Main module to start front end of app.
## Access helper module to use options picked by user.
##

# Import modules
import npyscreen as npy
import helper

# Global variables
stock = ""
check = False

options = ['Info', 'Financials', 'Balance Sheet', 'Cash Flow', 'Earnings',
           'Analysis', 'Graph: MAX', 'Graph: 5Y', 'Graph: YTD', 'Graph: 1MO', 'Graph: 1D']
pick = ""

# Class for npyscreen stock form
class getStockForm(npy.ActionForm):
    def create(self):
        self.show_atx = 55
        self.show_aty = 15

        self.name = self.add(npy.TitleText, name="Stock: ", relx=20)
        self.opt = self.text = self.add(npy.MultiSelect, values=options)


    def on_ok(self):
        global stock, pick
        stock = self.name.value.upper()
        pick = self.opt.value

        helper.load(stock)

        check = helper.checkStock()

        if check == True:
            self.parentApp.setNextForm(None)
        else:
            self.name.value = "Re-Enter"


    def on_cancel(self):
        exit()


# Class to start npyscreen stock form
class App(npy.NPSAppManaged):
    def onStart(self):
        self.addForm('MAIN', getStockForm, lines=20, columns=80)

# Method to run app
def app():
    a = App().run()

# Run only if started as __main__
if __name__ == "__main__":
    app()

    helper.helper(pick)