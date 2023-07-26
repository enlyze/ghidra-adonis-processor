#Rename functions that pass their name to a logging function - You may need to adjust constants
#@author Tom Dohrmann
#@category Adonis
#@keybinding 
#@menupath 
#@toolbar 

# Rename this function for your firmware.
LOG_FUNCTION_NAME = "FUN_14debd40"

import ghidra.app.decompiler.DecompInterface as DecompInterface
import ghidra.program.model.listing.Function as Function
import ghidra.program.model.pcode.HighFunction as HighFunction
import ghidra.program.model.pcode.PcodeOp as PcodeOp
import ghidra.program.model.symbol.RefType as RefType
import ghidra.program.model.symbol.SourceType as SourceType

def get_calling_functions(program, function):
    refs = program.getReferenceManager().getReferencesTo(function.getEntryPoint())
    calls = [ref.getFromAddress() for ref in refs if ref.getReferenceType() == RefType.UNCONDITIONAL_CALL]
    return [program.getListing().getFunctionContaining(addr) for addr in calls]

def get_second_arg(program, fun):
    dec = DecompInterface()
    dec.openProgram(program)
    result = dec.decompileFunction(fun, 0, monitor)
    c = result.getDecompiledFunction().getC()
    idx = c.index("LOG_FUNCTION_NAME")
    c = c[idx:]
    idx = c.index("\"")
    c = c[idx+1:]
    idx = c.index("\"")
    c = c[:idx]
    print(c)
    fun.setName(c, SourceType.ANALYSIS)

fun = getFunctionAt(toAddr("LOG_FUNCTION_NAME"))
calling_funs = get_calling_functions(currentProgram, fun)

for calling_fun in calling_funs:
    get_second_arg(currentProgram, calling_fun)