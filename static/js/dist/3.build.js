webpackJsonp([3],{

/***/ 19:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
Object.defineProperty(__webpack_exports__, "__esModule", { value: true });
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__babel_loader_node_modules_vue_loader_lib_selector_type_script_index_0_Contact_vue__ = __webpack_require__(25);
/* empty harmony namespace reexport */
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_1__node_modules_vue_loader_lib_template_compiler_index_id_data_v_a2b1f6c6_hasScoped_false_buble_transforms_node_modules_vue_loader_lib_selector_type_template_index_0_Contact_vue__ = __webpack_require__(29);
var normalizeComponent = __webpack_require__(3)
/* script */


/* template */

/* template functional */
var __vue_template_functional__ = false
/* styles */
var __vue_styles__ = null
/* scopeId */
var __vue_scopeId__ = null
/* moduleIdentifier (server only) */
var __vue_module_identifier__ = null
var Component = normalizeComponent(
  __WEBPACK_IMPORTED_MODULE_0__babel_loader_node_modules_vue_loader_lib_selector_type_script_index_0_Contact_vue__["a" /* default */],
  __WEBPACK_IMPORTED_MODULE_1__node_modules_vue_loader_lib_template_compiler_index_id_data_v_a2b1f6c6_hasScoped_false_buble_transforms_node_modules_vue_loader_lib_selector_type_template_index_0_Contact_vue__["a" /* default */],
  __vue_template_functional__,
  __vue_styles__,
  __vue_scopeId__,
  __vue_module_identifier__
)

/* harmony default export */ __webpack_exports__["default"] = (Component.exports);


/***/ }),

/***/ 25:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__contact_css__ = __webpack_require__(27);
/* harmony import */ var __WEBPACK_IMPORTED_MODULE_0__contact_css___default = __webpack_require__.n(__WEBPACK_IMPORTED_MODULE_0__contact_css__);
//
//
//
//
//
//
//
//
//
//
//
//


/* harmony default export */ __webpack_exports__["a"] = ({
  name: 'contact',
  data() {
    return {
      firstname: 'Tim',
      lastname: 'Hooker',
      address: '860 Lockland',
      dob: '12-21-1978',
      phone: 'nunya',
      email: 'timhooker@me.com'
    };
  }
});

/***/ }),

/***/ 27:
/***/ (function(module, exports, __webpack_require__) {

// style-loader: Adds some css to the DOM by adding a <style> tag

// load the styles
var content = __webpack_require__(28);
if(typeof content === 'string') content = [[module.i, content, '']];
if(content.locals) module.exports = content.locals;
// add the styles to the DOM
var update = __webpack_require__(5)("fc2c5c5e", content, true);

/***/ }),

/***/ 28:
/***/ (function(module, exports, __webpack_require__) {

exports = module.exports = __webpack_require__(4)(undefined);
// imports


// module
exports.push([module.i, ".contact-props li{display:block}", ""]);

// exports


/***/ }),

/***/ 29:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
var render = function () {var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;return _c('div',{staticClass:"contact"},[_c('h2',[_vm._v(_vm._s((_vm.firstname + " " + _vm.lastname)))]),_vm._v(" "),_c('ul',{staticClass:"contact-props"},[_c('li',[_vm._v(_vm._s(_vm.dob))]),_vm._v(" "),_c('li',[_vm._v(_vm._s(_vm.address))]),_vm._v(" "),_c('li',[_vm._v(_vm._s(_vm.phone))]),_vm._v(" "),_c('li',[_vm._v(_vm._s(_vm.email))])])])}
var staticRenderFns = []
var esExports = { render: render, staticRenderFns: staticRenderFns }
/* harmony default export */ __webpack_exports__["a"] = (esExports);

/***/ })

});
//# sourceMappingURL=3.build.js.map