from mdstudio.deferred.chainable import chainable
from mdstudio.component.session import ComponentSession
from mdstudio.runner import main
import os

workdir = "/tmp/lie_amber"
structure_path = os.path.join(os.getcwd(), "input.mol2")
with open(structure_path, 'r') as f:
    amber_input = f.read()

structure = {"path": structure_path, "content": amber_input,
             "extension": ".mol2"}


class Run_acpype(ComponentSession):

    def authorize_request(self, uri, claims):
        return True

    @chainable
    def on_run(self):
        result = yield self.call(
            "mdgroup.lie_amber.endpoint.acpype",
            {"structure": structure,
             "workdir": workdir})
        print(result)
        # assert all(os.path.isfile(p) or os.path.isdir(p) for p in result.values())


if __name__ == "__main__":
    main(Run_acpype)
