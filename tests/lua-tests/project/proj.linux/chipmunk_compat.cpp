/* Chipmunk glibc 2.34+ compatibility shim */
#include <math.h>

extern "C" {
    float __powf_finite(float x, float y) { return powf(x, y); }
    float __expf_finite(float x) { return expf(x); }
}
