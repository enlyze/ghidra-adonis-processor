# Ghidra ADONIS Processor

This repo contains modified x86 SLEIGH files for use with the ADONIS kernel.

ADONIS uses a x32-ish ABI that uses 32-bit points in long mode. Ghidra doesn't cope with that very well, tries to cast pointer betweens ints and longs and looses all type information (such as pointers to structs) as a result. The SLEIGH files have been modified to use a 32-bit memory and all memory accesses have been truncated to 32-bit.

ADONIS is the name of the operating system found on Siemens PLCs. The ghidra-adonis-processor project is not in any way affiliated with or endorsed by Siemens.
