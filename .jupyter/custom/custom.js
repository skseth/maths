alert("hello world IV from custom.js")


// window.MathJax = {
//     TeX: {
//         "extensions": [
//             "physics.js"
//         ]
//     }
// };


// MathJax.Hub.Config({
//     TeX: {
//       Macros: {
//         RR: '{\\bf R}',
//         bold: ['{\\bf #1}', 1]
//       }
//     }
//   });
//   MathJax.Hub.Configured()


define([
   'base/js/namespace',
   'base/js/promises'
], function(IPython, promises) {
    promises.app_initialized.then(function (appName) {
        if (appName !== 'NotebookApp') return;
        MathJax.Hub.Config({
            TeX: { equationNumbers: { autoNumber: "AMS" } }
        });

        // console.log("calling Mathjax Hub Config")

        // MathJax.Hub.Config({
        //     TeX: {
        //       Macros: {
        //         RR: '{\\bf R}',
        //         bold: ['{\\bf #1}', 1]

        //       }
        //     }
        //   });


        MathJax.Hub.Register.StartupHook("TeX Jax Ready", function () {
            MathJax.InputJax.TeX.Definitions.Add({
              macros: {
                dv: ["Macro", '{\\frac{\\mathrm{d}{#1}}{\\mathrm{d}{#2}}}', 2],
                pd: ["Macro", '{\\frac{\\partial{#1}}{\\partial{#2}}}', 2]
              }
            });
          });

    });
});



// $([IPython.events]).on('app_initialized.NotebookApp', function(){
//     alert("in mathjax config")
//     MathJax.Hub.Config({
//         tex2jax: {
//             inlineMath: [["$", "$"], ["\\(", "\\)"]],
//             displayMath: [["$$", "$$"], ["\\[", "\\]"]],
//             processEscapes: true,
//         },
//         TeX: {
//             Macros: {
//                 Alpha: "\\mbox{A}",
//                 Beta: "\\mbox{B}",
//                 Epsilon: "\\mbox{E}",
//                 Zeta: "\\mbox{Z}",
//                 Eta: "\\mbox{H}",
//                 Iota: "\\mbox{I}",
//                 Kappa: "\\mbox{K}",
//                 Mu: "\\mbox{M}",
//                 Nu: "\\mbox{N}",
//                 Omicron: "\\mbox{O}",
//                 Rho: "\\mbox{P}",
//                 Tau: "\\mbox{T}",
//                 Chi: "\\mbox{X}",
//                 and: "\\mbox{&}",
//                 or: "\\lor",
//                 exist: "\\exists",
//                 empty: "\\emptyset",
//                 P: "\\mbox{P}",
//                 tan: "\\operatorname{tg}",   // tangent
//                 tg: "\\operatorname{tg}",    // tangent
//                 cot: "\\operatorname{ctg}",  // cotangent
//                 ctg: "\\operatorname{ctg}",  // cotangent
//                 csc: "\\operatorname{cosec}",     // cosecant
//                 cosec: "\\operatorname{cosec}",   // cosecant
//                 arctan: "\\operatorname{arctg}",  // arctangent
//                 arctg: "\\operatorname{arctg}",   // arctangent
//                 arccot: "\\operatorname{arcctg}",      // arc cotangent
//                 arcctg: "\\operatorname{arcctg}",      // arc cotangent
//                 arcsec: "\\operatorname{arcsec}",      // arc secant
//                 arccsc: "\\operatorname{arccosec}",    // arc cosecant
//                 arccosec: "\\operatorname{arccosec}",  // arc cosecant
//                 sh: "\\operatorname{sh}",     // hyperbolic sine
//                 ch: "\\operatorname{ch}",     // hyperbolic cosine
//                 th: "\\operatorname{th}",     // hyperbolic tangent
//                 cth: "\\operatorname{cth}",   // hyperbolic cotangent
//                 sinh: "\\operatorname{sh}",   // hyperbolic синус
//                 cosh: "\\operatorname{ch}",   // hyperbolic cosine
//                 tanh: "\\operatorname{th}",   // hyperbolic tangent
//                 coth: "\\operatorname{cth}",  // hyperbolic cotangent
//                 sgn: "\\operatorname{sgn}",
//                 mod: "\\operatorname{mod}",
//                 ge: "\\geqslant",
//                 le: "\\leqslant",
//                 geq: "\\geqslant",
//                 leq: "\\leqslant",
//                 N: "\\mathbb{N}",
//                 R: "\\mathbb{R}",
//                 Q: "\\mathbb{Q}",
//                 Z: "\\mathbb{Z}",
//                 C: "\\mathbb{C}",
//                 H: "\\mathbb{H}",
//                 P: "\\mathbb{P}",
//                 dmtr: "\\unicode{x2300}", // diameter sign
//                 deg: "\\unicode{xb0}",    // degree sign
//                 celdeg: "\\unicode{x2103}"   // degree Celsius sign
//             },
//             // AutoNumbering of displayed formulas
//             equationNumbers: { autoNumber: "AMS" },
//             // All mathjax extensions:
//             // http://docs.mathjax.org/en/latest/tex.html#tex-and-latex-extensions
//             // Source code for all extensions:
//             // https://github.com/mathjax/MathJax/tree/master/extensions/TeX
//             extensions: [
//                 "color.js", // Color support in LaTeX
//                 "autobold.js", // support for \boldsymbol{...}
//                 "AMSmath.js",
//                 "AMSsymbols.js",
//                 "AMScd.js", // http://www.jmilne.org/not/Mamscd.pdf
//                 "bbox.js", // support for \bbox[options]{math}
//                 // "begingroup.js", // mainly for formulas localization
//                 "cancel.js" // support for strikethrough formulas
//                 // "HTML.js" // works by default
//                 // "mhchem.js" // chemical formulas
//                 // "uniconde.js" // works by default
//             ]
//         }
//     });
//     // http://docs.mathjax.org/en/latest/configuration.html#configuring-mathjax-after-it-is-loaded
//     MathJax.Hub.Configured()
// });