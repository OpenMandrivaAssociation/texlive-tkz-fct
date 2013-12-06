# revision 22831
# category Package
# catalog-ctan /macros/latex/contrib/tkz/tkz-fct
# catalog-date 2011-06-05 23:10:23 +0200
# catalog-license lppl
# catalog-version 1.16c
Name:		texlive-tkz-fct
Version:	1.16c
Release:	6
Summary:	Tools for drawing graphs of functions
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/tkz/tkz-fct
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-fct.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/tkz-fct.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The tkz-fct package is designed to give math teachers (and
students) easy access at the programmation of graphs of
functions with TikZ and gnuplot.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/tkz-fct/tkz-fct.sty
%doc %{_texmfdistdir}/doc/latex/tkz-fct/README
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/Makefile
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/info_fct_tex.txt
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-1-0-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-10-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-10-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-10-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-10-5-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-10-6-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-10-7-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-10-8-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-11-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-11-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-11-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-11-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-11-5-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-11-6-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-11-7-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-12-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-12-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-12-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-12-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-12-5-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-12-6-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-13-0-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-5-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-6-1.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-7-1.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-7-2.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-7-3.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-7-4.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-8-1.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-14-8-2.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-15-0-3.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-15-0-4.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-16-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-16-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-3-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-3-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-4-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-4-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-4-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-4-5-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-4-6-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-4-7-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-4-8-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-5-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-5-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-5-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-5-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-5-5-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-5-6-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-6-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-7-10-2.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-7-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-7-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-7-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-7-5-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-7-6-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-7-7-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-7-8-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-7-9-1.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-8-10-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-8-11-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-8-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-8-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-8-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-8-6-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-8-7-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-8-8-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-8-9-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-9-1-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-9-2-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-9-3-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/latex/tkzFct-9-4-0.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/examples/tkzfctpreamble.ltx
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-VDW.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-area.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-asymptote.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-bac.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-compilation.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-example.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-faq.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-fonctions.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-fppgf.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-installation.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-interpolation.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-label.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-liste.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-main.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-param.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-point.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-polar.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-riemann.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-symbol.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-tangent.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/TKZdoc-fct-why.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/latex/fct.ist
%doc %{_texmfdistdir}/doc/latex/tkz-fct/readme-tkz-fct-fr.txt
%doc %{_texmfdistdir}/doc/latex/tkz-fct/readme-tkz-fct.txt
%doc %{_texmfdistdir}/doc/latex/tkz-fct/readme.tex
%doc %{_texmfdistdir}/doc/latex/tkz-fct/tkz-fct-screen.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 05 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.16c-2
+ Revision: 756978
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.16c-1
+ Revision: 719764
- texlive-tkz-fct
- texlive-tkz-fct
- texlive-tkz-fct

