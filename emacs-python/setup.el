(require 'package)
(add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/"))
(package-initialize)
(unless package-archive-contents
  (package-refresh-contents))
(dolist (package '(use-package elpy pyvenv blacken flycheck))
  (unless (package-installed-p package)
    (package-install package)))

(use-package elpy
  :ensure t
  :init
  (elpy-enable))

(use-package pyvenv
  :ensure t
  :config
  (setenv "WORKON_HOME" "~/.virtualenvs")
  (pyvenv-activate "~/.virtualenvs/myenv")  ; Set myenv as default environment
  (pyvenv-mode 1))

(use-package blacken
  :ensure t
  :hook (python-mode . blacken-mode))

(use-package flycheck
  :ensure t
  :init (global-flycheck-mode))

(global-display-line-numbers-mode)
(show-paren-mode 1)

(use-package pyvenv
  :ensure t
  :config
  (pyvenv-activate "~/.virtualenvs/myenv")  ; Ensure myenv is activated globally
  (pyvenv-mode 1))

(use-package elpy
  :ensure t
  :init
  (elpy-enable))

(use-package company
  :ensure t
  :init (global-company-mode))

(use-package company-jedi
  :ensure t
  :config
  (add-to-list 'company-backends 'company-jedi))

(use-package lsp-mode
  :ensure t
  :hook (python-mode . lsp-deferred)
  :commands (lsp lsp-deferred))

(use-package lsp-pyright
  :ensure t
  :hook (python-mode . (lambda ()
        (require 'lsp-pyright)
        (lsp))))
