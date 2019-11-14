import globals
import lda
import Converter

if __name__ == "__main__":
    globals.initialize()
    globals.a = Converter.stack_matrices()

    max = Converter.findmax(globals.a)

    result = Converter.normalize(max)
    Converter.rms(result)
    Converter.mav(result)
    Converter.std(result)
    Converter.var(result)
    lda.classifier()


