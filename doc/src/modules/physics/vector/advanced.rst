============================================================================
Potential Issues/Advanced Topics/Future Features in Physics/Mechanics Module
============================================================================

This document will describe some of the more advanced functionality that this
module offers but which is not part of the "official" interface. Here, some of
the features that will be implemented in the future will also be covered, along
with unanswered questions about proper functionality. Also, common problems
will be discussed, along with some solutions.

Common Issues
=============
Here issues with numerically integrating code, choice of `dynamicsymbols` for
coordinate and speed representation, printing, differentiating, and
substitution will occur.

Numerically Integrating Code
----------------------------
See Future Features: Code Output

Printing
--------
The default printing options are to use sorting for ``Vector`` and ``Dyad``
measure numbers, and have unsorted output from the ``vprint``, ``vpprint``, and
``vlatex`` functions. If you are printing something large, please use one of
those functions, as the sorting can increase printing time from seconds to
minutes.

Differentiating
---------------
Differentiation of very large expressions can take some time in SymPy; it is
possible for large expressions to take minutes for the derivative to be
evaluated. This will most commonly come up in linearization.

Substitution
------------
Substitution into large expressions can be slow, and take a few minutes.

Acceleration of Points
----------------------
At a minimum, points need to have their velocities defined, as the acceleration
can be calculated by taking the time derivative of the velocity in the same
frame. If the 1 point or 2 point theorems were used to compute the velocity,
the time derivative of the velocity expression will most likely be more complex
than if you were to use the acceleration level 1 point and 2 point theorems.
Using the acceleration level methods can result in shorted expressions at this
point, which will result in shorter expressions later (such as when forming
Kane's equations).


Advanced Interfaces
===================

Here we will cover advanced options in: ``ReferenceFrame``, ``dynamicsymbols``,
and some associated functionality.

ReferenceFrame
--------------
``ReferenceFrame`` is shown as having a ``.name`` attribute and ``.x``, ``.y``,
and ``.z`` attributes for accessing the basis vectors, as well as a fairly
rigidly defined print output. If you wish to have a different set of indices
defined, there is an option for this. This will also require a different
interface for accessing the basis vectors. ::

  >>> from sympy.physics.vector import ReferenceFrame, vprint, vpprint, vlatex
  >>> N = ReferenceFrame('N', indices=['i', 'j', 'k'])
  >>> N['i']
  N['i']
  >>> N.x
  N['i']
  >>> vlatex(N.x)
  '\\mathbf{\\hat{n}_{i}}'

Also, the latex output can have custom strings; rather than just indices
though, the entirety of each basis vector can be specified. The custom latex
strings can occur without custom indices, and also overwrites the latex string
that would be used if there were custom indices. ::

  >>> from sympy.physics.vector import ReferenceFrame, vlatex
  >>> N = ReferenceFrame('N', latexs=['n1','\mathbf{n}_2','cat'])
  >>> vlatex(N.x)
  'n1'
  >>> vlatex(N.y)
  '\\mathbf{n}_2'
  >>> vlatex(N.z)
  'cat'

dynamicsymbols
--------------
The ``dynamicsymbols`` function also has 'hidden' functionality; the variable
which is associated with time can be changed, as well as the notation for
printing derivatives. ::

  >>> from sympy import symbols
  >>> from sympy.physics.vector import dynamicsymbols, vprint
  >>> q1 = dynamicsymbols('q1')
  >>> q1
  q1(t)
  >>> dynamicsymbols._t = symbols('T')
  >>> q2 = dynamicsymbols('q2')
  >>> q2
  q2(T)
  >>> q1
  q1(t)
  >>> q1d = dynamicsymbols('q1', 1)
  >>> vprint(q1d)
  q1'
  >>> dynamicsymbols._str = 'd'
  >>> vprint(q1d)
  q1d
  >>> dynamicsymbols._str = '\''
  >>> dynamicsymbols._t = symbols('t')


Note that only dynamic symbols created after the change are different. The same
is not true for the `._str` attribute; this affects the printing output only,
so dynamic symbols created before or after will print the same way.

Also note that ``Vector``'s ``.dt`` method uses the ``._t`` attribute of
``dynamicsymbols``, along with a number of other important functions and
methods. Don't mix and match symbols representing time.


Future Features
===============

This will cover the planned features to be added to this submodule.

Code Output
-----------
A function for generating code output for numerical integration is the highest
priority feature to implement next. There are a number of considerations here.

Code output for C (using the GSL libraries), Fortran 90 (using LSODA), MATLAB,
and SciPy is the goal. Things to be considered include: use of ``cse`` on large
expressions for MATLAB and SciPy, which are interpretive. It is currently unclear
whether compiled languages will benefit from common subexpression elimination,
especially considering that it is a common part of compiler optimization, and
there can be a significant time penalty when calling ``cse``.

Care needs to be taken when constructing the strings for these expressions, as
well as handling of input parameters, and other dynamic symbols. How to deal
with output quantities when integrating also needs to be decided, with the
potential for multiple options being considered.


