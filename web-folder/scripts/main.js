// Main JavaScript

document.addEventListener('DOMContentLoaded', function() {
    console.log('Casino website loaded');
    
    // Add smooth scrolling to all links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            
            document.querySelector(this.getAttribute('href')).scrollIntoView({
                behavior: 'smooth'
            });
        });
    });
    
    // Add responsible gambling collapsible info
    const responsibleGamblingElements = document.querySelectorAll('.responsible-gambling-toggle');
    if (responsibleGamblingElements.length > 0) {
        responsibleGamblingElements.forEach(element => {
            element.addEventListener('click', function() {
                const content = this.nextElementSibling;
                if (content.style.maxHeight) {
                    content.style.maxHeight = null;
                } else {
                    content.style.maxHeight = content.scrollHeight + "px";
                }
            });
        });
    }
});

// Component scripts will be added by the import_components function